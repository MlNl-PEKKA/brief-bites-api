from fastapi import FastAPI
import json
import requests
import xmltodict
from bs4 import BeautifulSoup
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from transformers import pipeline

app = FastAPI()
@app.post("/")
def summarization():
    print('Arrival')
    label = None
    topics = [
        {
            'flag': 0,
            'label':'TOP STORIES',
            'category':'Top stories'
        },
        {
            'flag': 1,
            'label':'KARNATAKA',
            'category':'Local'
        },
        {
            'flag': 1,
            'label':'INDIA',
            'category':'National'
        },
        {
            'flag': 2,
            'label':'WORLD',
            'category':'International'
        },
        {
            'flag': 2,
            'label':'BUSINESS',
            'category':'Business'
        },
        {
            'flag': 2,
            'label':'POLITICS',
            'category':'Politics'
        },
        {
            'flag': 2,
            'label':'TECHNOLOGY',
            'category':'Technology'
        },
        {
            'flag': 2,
            'label':'HEALTH',
            'category':'Health'
        },
        {
            'flag': 2,
            'label':'SPORTS',
            'category':'Sports'
        },
        {
            'flag': 2,
            'label':'SCIENCE',
            'category':'Science'
        },
        {
            'flag': 2,
            'label':'ENTERTAINMENT',
            'category':'Entertainment'
        }
    ]
    result = {}
    for topic in topics:
        print(topic)
        label = topic['label']
        if(topic['flag']==0):
            url = 'https://news.google.com/rss?gl=US&hl=en-IN&ceid=IN:en'
        elif(topic['flag']==1):
            url =  f'https://news.google.com/rss/section/geo/{label}?gl=IN&hl=en-IN&ceid=IN:en'
        else:
            url = f'https://news.google.com/rss/section/topic/{label}?gl=IN&hl=en-IN&ceid=IN:en'
        response = requests.get(url)
        news_json = json.loads(json.dumps(xmltodict.parse(response.content)))
        top_news={}
        i=0
        x=1 #9
        while i<x:
            print(f'i:{i}')
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
                k= 10 if len(feed2)>=10 else len(feed2) #10
                while j<k:
                    print(f'j:{j}')
                    print("IGI")
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
                            doc['summary'] = None
                        print(f'DOC:{doc}')
                        news[str(j)]=doc
                        j=j+1
                    except:
                        break
                top_news[str(i)]=news
            else:
                x=x+1
            i=i+1
        result[topic['category']]=top_news
    return(result)
def lexrank(ot):
    from sumy.summarizers.lex_rank import LexRankSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    lex_rank_summarizer = LexRankSummarizer()
    summary_bundle = lex_rank_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return summary
def bart(ot):
    print("SUMMMM")
    summary_bundle=pipeline('summarization',model="philschmid/bart-large-cnn-samsum")
    return summary_bundle(ot[:4000])[0]['summary_text']