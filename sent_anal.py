"""
WORLD - https://news.google.com/news/rss
INDIA, KARNATAKA - https://news.google.com/news/rss/headlines/section/geo/{location}
TOPICS - https://news.google.com/news/rss/headlines/section/topic/{topic}
TOP STORIES, INTERNATIONAL, NATIONAL, LOCAL, BUSINESS, POLITICS, TECHNOLOGY, HEALTH, SPORTS, SCIENCE, ENTERTAINMENT
"""
from fastapi import FastAPI
from pydantic import BaseModel
import json
import requests
import xmltodict
from bs4 import BeautifulSoup
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from transformers import pipeline
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('serviceAccount.json')
#app = firebase_admin.initialize_app(cred)
db = firestore.client()


app = FastAPI()

class Request(BaseModel):
    topic : str
    article_count : int

def klsum(text):
    from sumy.summarizers.kl import KLSummarizer
    parser=PlaintextParser.from_string(text,Tokenizer('english'))
    kl_summarizer=KLSummarizer()
    summary_bundle= kl_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return(summary)
def lexrank(text):
    from sumy.summarizers.lex_rank import LexRankSummarizer
    parser=PlaintextParser.from_string(text,Tokenizer('english'))
    lex_rank_summarizer = LexRankSummarizer()
    summary_bundle = lex_rank_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return(summary)
def lsa(text):
    from sumy.summarizers.lsa import LsaSummarizer
    parser=PlaintextParser.from_string(text,Tokenizer('english'))
    lsa_summarizer=LsaSummarizer()
    summary_bundle=lsa_summarizer(parser.document,sentences_count=3) 
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return(summary)
def luhn(text):
    from sumy.summarizers.luhn import LuhnSummarizer
    parser=PlaintextParser.from_string(text,Tokenizer('english'))
    luhn_summarizer=LuhnSummarizer()
    summary_bundle=luhn_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return(summary)
def bart(text):
    summary_bundle=pipeline('summarization',model="philschmid/bart-large-cnn-samsum")
    return(summary_bundle(text[:3900])[0]['summary_text'])
#request:Request
@app.post("/")
def summarization():
    print('Arrival')
    country = 'IN'
    #url = f'https://news.google.com/rss?q={topic}&gl={country}'
    url_0 = f'https://news.google.com/rss?gl={country}hl=en-{country}&ceid={country}:en'
    response = requests.get(url_0)
    news_json = json.loads(json.dumps(xmltodict.parse(response.content)))
    i=0
    x=3
    top_news={}
    while i<x:
        soup = BeautifulSoup(news_json['rss']['channel']['item'][i]['description'], 'html.parser')
        feed = (soup.find_all("a")[-1]).get('href')
        if 'https://news.google.com/stories/' in feed:
            news={}
            title_0 = (str(news_json['rss']['channel']['item'][i]['title']).rsplit("-",1))[0]
            news['title']=title_0
            response2 = requests.get(feed)
            soup2 = BeautifulSoup(response2.text, 'html.parser')
            feed2 = soup2.find_all("a",{"class":"VDXfz"})
            sources = soup2.find_all("a",{"class":"wEwyrc AVN2gc WfKKme"})
            j=0
            k= 9 if len(feed2)>=9 else len(feed2)
            while j<k:
                try:
                    doc = {}
                    doc['url'] = str(feed2[j].get('href')).replace('.','https://news.google.com')
                    article = Article(doc['url'])
                    doc['source'] = str(sources[j].text)
                    article.download()
                    article.parse()
                    doc['title']=str(article.title)
                    text=str(article.text).replace('"','').replace('\n','').replace('/','')
                    doc['image']=str(article.top_image)
                    doc['time']=article.publish_date
                    if(j==0):
                        doc['type']=0
                        doc['summary'] = bart(text)
                    elif(j>0 and j<4):
                        doc['type']=1
                        doc['summary'] = lexrank(text)
                    else:
                        doc['type']=2
                        article.nlp()
                        doc['summary'] = article.summary
                    news[str(j)]=doc
                    j=j+1
                except:
                    break
            top_news[str(i)]=news
        else:
            x=x+1
        i=i+1
    return(top_news)