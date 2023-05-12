from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from transformers import pipeline
import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import re
import hashlib

cred = credentials.Certificate('serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()


app = FastAPI()

class Request(BaseModel):
    topic : str
    article_count : int

apikey_news = ['23d7176b507441d8a8596bc6587f73f4','8d68eec8aa76471693ef37934edd9d41','4456512be3b848ac97ea4adccdefd704','d8ca37e8c479471da02f4cebd6d8fbe9']

@app.post("/")
def summary(request:Request):
    general_ref = db.collection('general')
    docs = general_ref.stream()
    documents = {}
    request.topic=(re.sub('[^A-Za-z0-9 ]','',request.topic)).lower()
    hex_dig = (hashlib.sha1(request.topic.encode('utf-8'))).hexdigest()
    for doc in docs:
        documents[doc.id]=doc.to_dict()
    if hex_dig in documents.keys() and len(documents[hex_dig].keys())>=request.article_count+1:
        return documents[hex_dig]
    else:
        return summarize(request,hex_dig)
    
def summarize(request:Request,hex_dig):
    news_api = f'https://newsapi.org/v2/everything?q={request.topic}&language=en&pageSize={request.article_count}&apiKey={apikey_news[0]}'
    response = requests.get(news_api)
    news = json.loads(response.content)
    results = {}
    results['topic'] = request.topic
    for article_info in news['articles']:
        article = Article(article_info['url'])
        article.download()
        article.parse()
        ot = (article.text).replace('"','').replace('\n','').replace('/','')
        if len(ot)<500:
            ot = fall_back_news_length(article_info['url'])
        result = {}
        result['link'] = article_info['url']
        result['img'] = article_info['urlToImage'] if article_info['urlToImage'] != None  else 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.facebook.com%2F102607211615964%2Fphotos%2Fa.102617174948301%2F102617794948239%2F%3Ftype%3D3&psig=AOvVaw3g6BTOvtlcqAhGTcuIPRx7&ust=1679343744572000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCMCw7qbp6P0CFQAAAAAdAAAAABAR'
        result['publishedAt'] = article_info['publishedAt']
        result['author'] = article_info['author'] if article_info['author']!=None else 'Anonymous'
        result['source'] = article_info['source']['name']
        result['ot'] = ot
        klsum(result,ot)
        lexrank(result,ot)
        lsa(result,ot)
        luhn(result,ot)
        summary_functions = [bart,pegasus]
        threads = []
        for summary_function in summary_functions:
            thread = threading.Thread(target=summary_function,args=[result,ot])
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        results[str(len(results)-1)]=result
    db.collection('general').document(str(hex_dig)).set(results)
    return results

def klsum(result,ot):
    from sumy.summarizers.kl import KLSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    kl_summarizer=KLSummarizer()
    summary_bundle= kl_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    result['klsum']=summary
def lexrank(result,ot):
    from sumy.summarizers.lex_rank import LexRankSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    lex_rank_summarizer = LexRankSummarizer()
    summary_bundle = lex_rank_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    result['lexrank']=summary
def lsa(result,ot):
    from sumy.summarizers.lsa import LsaSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    lsa_summarizer=LsaSummarizer()
    summary_bundle=lsa_summarizer(parser.document,sentences_count=3) 
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    result['lsa']=summary
def luhn(result,ot):
    from sumy.summarizers.luhn import LuhnSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    luhn_summarizer=LuhnSummarizer()
    summary_bundle=luhn_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    result['luhn']=summary
def bart(result,ot):
    summary_bundle=pipeline('summarization',model="philschmid/bart-large-cnn-samsum")
    result['bart']= summary_bundle(ot[:4000])[0]['summary_text']
def pegasus(result,ot):
    summary_bundle=pipeline('summarization',model="google/pegasus-cnn_dailymail")
    result['pegasus']= summary_bundle(ot[:4000])[0]['summary_text'].replace('<n>','')

def fall_back_news_length(url):
    import requests
    from bs4 import BeautifulSoup
    response = requests.get(url)
    doc = BeautifulSoup(response.text, 'html.parser')
    par = doc.find_all('p')
    list = []
    for p in par:
        if len(p.text)!=0 and p.text[-1]=='.':
            list.append(p.text)
    return(''.join(list))