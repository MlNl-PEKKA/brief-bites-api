import json
import requests
import xmltodict
import hashlib
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from newspaper import Article
from fastapi import FastAPI
from transformers import pipeline
from rouge_score import rouge_scorer
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import openai
from pydantic import BaseModel
cred = credentials.Certificate('serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
openai.api_key = "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"
#openai.api_key="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"
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'],use_stemmer=True)
from fastapi.middleware.cors import CORSMiddleware
origins = ["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    url: str
@app.post("/community")
def community(item: Item):
    try:
        article = Article(item.url)
        article.download()
        article.parse()
        a = {}
        a['title']=article.title
        a['imgUrl']=article.top_image
        a['link']=item.url
        a['time']=article.publish_date
        a['source']='Community'
        a['text']=article.text.replace('\n','. ').replace('"','\'').replace('. . ','. ')[:4000]
        techs = {'klsum':kl, 'lexrank':lex, 'lsa':ls,'luhn':luh,'bart':bar, 'pegasus':pegasu, 'chatGPT':chatGP}
        for tech in techs:
            s={}
            s['summary']=techs[tech](a['text'])
            a[tech]=s
        for tech in techs:
            rouge={}
            score={}
            rouge['vtext']=scorer.score(a['text'],a[tech]['summary'])
            score['vtext']=scor(rouge['vtext'])
            for t in techs:
                rouge[f'v{t}']=scorer.score(a[t]['summary'],a[tech]['summary'])
                score[f'v{t}']=scor(rouge[f'v{t}'])
            a[tech]['rouge']=rouge
            a[tech]['score']=score
            a[tech]['final_score']=skor(score)
        text_digest = hashlib.sha1(a['title'].encode()).hexdigest()
        a['id']=text_digest
        a['votes']=0
        db.collection('community').document(a['id']).set(a)
        print('🔥')
    except:
        print('💩')
def kl(ot):
    print(1)
    from sumy.summarizers.kl import KLSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    kl_summarizer=KLSummarizer()
    summary_bundle= kl_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return summary
def lex(ot):
    print(2)
    from sumy.summarizers.lex_rank import LexRankSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    lex_rank_summarizer = LexRankSummarizer()
    summary_bundle = lex_rank_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return summary
def ls(ot):
    print(3)
    from sumy.summarizers.lsa import LsaSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    lsa_summarizer=LsaSummarizer()
    summary_bundle=lsa_summarizer(parser.document,sentences_count=3) 
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return summary
def luh(ot):
    print(4)
    from sumy.summarizers.luhn import LuhnSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    luhn_summarizer=LuhnSummarizer()
    summary_bundle=luhn_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return summary
def bar(ot):
    print(5)
    summary_bundle=pipeline('summarization',model="philschmid/bart-large-cnn-samsum")
    summary = summary_bundle(ot[:4000])[0]['summary_text']
    return summary
def pegasu(ot):
    print(6)
    summary_bundle=pipeline('summarization',model="google/pegasus-cnn_dailymail")
    summary = summary_bundle(ot[:4000])[0]['summary_text'].replace('<n>','')
    return summary
def chatGP(ot):
    print(7)
    message = [ {"role": "system", "content": 
              "You are a text summarizer."},
              {"role": "user", "content":ot}]
    chat = openai.ChatCompletion.create(model = "gpt-3.5-turbo",messages=message)
    summary = chat['choices'][0]['message']['content']
    return(summary)
def scor(rouge):
    return (rouge['rouge1'][2]+rouge['rouge2'][2]+rouge['rougeL'][2])/3
def skor(sl):
    a = ['vklsum','vlexrank','vlsa','vluhn']
    b = ['vbart', 'vpegasus']
    c = ['vchatGPT']
    sum=0
    for s in sl:
        if s in a:
            sum+=sl[s]*0.1
        elif s in b:
            sum+=sl[s]*0.4
        elif s in c:
            sum+=sl[s]*0.4
    if(sum>1):
        sum=1.0
    return sum