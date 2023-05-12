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
cred = credentials.Certificate('serviceAccount.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()
#openai.api_key = "###"
openai.api_key="###"
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'],use_stemmer=True)
app = FastAPI()
@app.get("/articles")
def articles():
    return get_all_articles(9)
def get_all_articles(num):
    label = None
    topics = [
        {
            'flag': 0,
            'label':'TOP STORIES',
            'category':'top-stories',
            'pos':0
        },
        {
            'flag': 1,
            'label':'KARNATAKA',
            'category':'local',
            'pos':1
        },
        {
            'flag': 1,
            'label':'INDIA',
            'category':'national',
            'pos':2
        },
        {
            'flag': 2,
            'label':'WORLD',
            'category':'international',
            'pos':3
        },
        {
            'flag': 2,
            'label':'BUSINESS',
            'category':'business',
            'pos':4
        },
        {
            'flag': 2,
            'label':'POLITICS',
            'category':'politics',
            'pos':5
        },
        {
            'flag': 2,
            'label':'TECHNOLOGY',
            'category':'technology',
            'pos':6
        },
        {
            'flag': 2,
            'label':'HEALTH',
            'category':'health',
            'pos':7
        },
        {
            'flag': 2,
            'label':'SPORTS',
            'category':'sports',
            'pos':8
        },
        {
            'flag': 2,
            'label':'SCIENCE',
            'category':'science',
            'pos':9
        },
        {
            'flag': 2,
            'label':'ENTERTAINMENT',
            'category':'entertainment',
            'pos':10
        }
    ]
    link = 0
    result = {}
    memo={}
    res=[]
    for topic in topics:
        label = topic['label']
        if(topic['flag']==0):
            url = 'https://news.google.com/rss?gl=US&hl=en-IN&ceid=IN:en'
        elif(topic['flag']==1):
            url =  f'https://news.google.com/rss/section/geo/{label}?gl=IN&hl=en-IN&ceid=IN:en'
        else:
            url = f'https://news.google.com/rss/section/topic/{label}?gl=IN&hl=en-IN&ceid=IN:en'
        response = requests.get(url)
        news_json = json.loads(json.dumps(xmltodict.parse(response.content)))
        categ = {}
        categ['category']=topic['category']
        categ_news = []
        for item in news_json['rss']['channel']['item'][:num]:
            try:
                url_digest = hashlib.sha1(item['link'].encode()).hexdigest()
                if(url_digest in memo):
                    memoized_data=res[memo[url_digest]['pos']]['articles'][memo[url_digest]['id']]
                    c=memoized_data['common_category']
                    c.append(topic['common_category'])
                    res[memo[url_digest]['pos']]['articles'][memo[url_digest]['id']]['common_category']=c
                    categ_news.append(memoized_data)
                    db.collection(topic['category']).document(memoized_data['id']).set(memoized_data)
                    link = link+1
                    print(f'Memoized {link} ')
                    continue
                article = Article(item['link'])
                article.download()
                article.parse()
                link = link+1
                print(link)
                obj = {}
                obj['title']=item['title']
                obj['link']=item['link']
                obj['time']=item['pubDate']
                obj['source']=item['source']['#text']
                c = []
                c.append(topic['category'])
                obj['common_category']=c
                obj['text']=article.text.replace('\n','. ').replace('"','\'').replace('. . ','. ')[:4000]
                techs = {'klsum':kl, 'lexrank':lex, 'lsa':ls,'luhn':luh,'bart':bar, 'pegasus':pegasu, 'chatGPT':chatGP}
                for tech in techs:
                    s={}
                    s['summary']=techs[tech](obj['text'])
                    obj[tech]=s
                for tech in techs:
                    s={}
                    s['vtext']=score(scorer.score(obj['text'], obj[tech]['summary']))
                    s['vklsum']=score(scorer.score(obj[tech]['summary'], obj['klsum']['summary']))*0.0625
                    s['vlexrank']=score(scorer.score(obj[tech]['summary'], obj['lexrank']['summary']))*0.0625
                    s['vlsa']=score(scorer.score(obj[tech]['summary'], obj['lsa']['summary']))*0.0625
                    s['vluhn']=score(scorer.score(obj[tech]['summary'],obj['luhn']['summary']))*0.0625
                    s['vbart']=score(scorer.score(obj[tech]['summary'], obj['bart']['summary']))*0.125
                    s['vpegasus']=score(scorer.score(obj[tech]['summary'], obj['pegasus']['summary']))*0.125
                    s['vchatgpt']=score(scorer.score(obj[tech]['summary'],obj['chatGPT']['summary']))*0.5
                    s['final']=s['vklsum']+s['vlexrank']+s['vlsa']+s['vluhn']+s['vbart']+s['vpegasus']+s['vchatgpt']
                    obj[tech]['versus']=s
                text_digest = hashlib.sha1(obj['title'].encode()).hexdigest()
                obj['id']=text_digest
                obj['votes']=0
                categ_news.append(obj)
                lol={}
                lol['pos']=topic['pos']
                lol['id']=len(categ_news)-1
                memo[url_digest]=lol
                db.collection(topic['category']).document(obj['id']).set(obj)
                print('Success')
            except:
               print('Failure')
               continue
        categ['articles']=categ_news
        res.append(categ)
    result['results']=res
    #store_toDB(result)
    return(result)
def store_toDB(results):
    try:
        for result in results['results']:
            for article in result['articles']:
                db.collection(result['category']).document(article['id']).set(article)
        print('Firebase success')
    except:
        print('Firebase failure')
def kl(ot):
    from sumy.summarizers.kl import KLSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    kl_summarizer=KLSummarizer()
    summary_bundle= kl_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return summary
def lex(ot):
    from sumy.summarizers.lex_rank import LexRankSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    lex_rank_summarizer = LexRankSummarizer()
    summary_bundle = lex_rank_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return summary
def ls(ot):
    from sumy.summarizers.lsa import LsaSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    lsa_summarizer=LsaSummarizer()
    summary_bundle=lsa_summarizer(parser.document,sentences_count=3) 
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return summary
def luh(ot):
    from sumy.summarizers.luhn import LuhnSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    luhn_summarizer=LuhnSummarizer()
    summary_bundle=luhn_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    return summary
def bar(ot):
    summary_bundle=pipeline('summarization',model="philschmid/bart-large-cnn-samsum")
    summary = summary_bundle(ot[:4000])[0]['summary_text']
    return summary
def pegasu(ot):
    summary_bundle=pipeline('summarization',model="google/pegasus-cnn_dailymail")
    summary = summary_bundle(ot[:4000])[0]['summary_text'].replace('<n>','')
    return summary
def chatGP(ot):
    message = [ {"role": "system", "content": 
              "You are a text summarizer."},
              {"role": "user", "content":ot}]
    chat = openai.ChatCompletion.create(model = "gpt-3.5-turbo",messages=message)
    summary = chat['choices'][0]['message']['content']
    print(f'ChatGPT: {summary}')
    return(summary)
def score(rouge):
    return (rouge['rouge1'][1]+rouge['rouge2'][1]+rouge['rougeL'][1])/3