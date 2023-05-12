import json
import requests
import xmltodict
from bs4 import BeautifulSoup
from newspaper import Article
from fastapi import FastAPI
app = FastAPI()
@app.post("/")
def summarization():
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
    res = {}
    c=0
    result=[]
    for topic in topics:
        temp_result = {}
        label = topic['label']
        temp_result['category']=topic['category']
        if(topic['flag']==0):
            url = 'https://news.google.com/rss?gl=US&hl=en-IN&ceid=IN:en'
        elif(topic['flag']==1):
            url =  f'https://news.google.com/rss/section/geo/{label}?gl=IN&hl=en-IN&ceid=IN:en'
        else:
            url = f'https://news.google.com/rss/section/topic/{label}?gl=IN&hl=en-IN&ceid=IN:en'
        response = requests.get(url)
        news_json = json.loads(json.dumps(xmltodict.parse(response.content)))
        top_news=[]
        i=0
        x=1 #9
        while i<x:
            print(f'i:{i}')
            news={}
            soup = BeautifulSoup(news_json['rss']['channel']['item'][i]['description'], 'html.parser')
            feed = (soup.find_all("a")[-1]).get('href')
            if 'https://news.google.com/stories/' in feed:
                title_0 = (str(news_json['rss']['channel']['item'][i]['title']).rsplit("-",1))[0]
                news['title']=title_0
                response2 = requests.get(feed)
                soup2 = BeautifulSoup(response2.text, 'html.parser')
                feed2 = soup2.find_all("a",{"class":"VDXfz"})
                sources = soup2.find_all("a",{"class":"wEwyrc AVN2gc WfKKme"})
                articles=[]
                j=0
                k= 1 if len(feed2)>=10 else len(feed2) #10
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
                            doc['summary'] = text
                        elif(j>0 and j<4):
                            doc['type']=1
                            doc['summary'] = text
                        else:
                            doc['type']=2
                            article.nlp()
                            doc['summary'] = None
                        print(f'DOC:{doc}')
                        articles.append(doc)
                        c=c+1
                        j=j+1
                    except:
                        break
                news['articles']=articles
                top_news.append(news)
            else:
                x=x+1
            i=i+1
        temp_result['news']=top_news
        result.append(temp_result)
    res['result']=result
    res['status']='ok' if len(result)!=0 else 'error'
    res['totalResults']=c
    return res
"""
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from transformers import pipeline


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

"""