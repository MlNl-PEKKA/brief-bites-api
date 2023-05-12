from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import json
import requests
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from rouge import Rouge
from transformers import pipeline
from rouge_score import rouge_scorer
rouge = Rouge()
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'],use_stemmer=True)
app = FastAPI()

class Post(BaseModel):
    topic : str
    article_count : int

apikey = '23d7176b507441d8a8596bc6587f73f4'

example = 'ChatGPT is a large language model developed by OpenAI, based on the GPT-3 architecture. This advanced conversational AI has revolutionized the field of natural language processing, offering a powerful tool for a wide range of applications. ChatGPT has a vast knowledge base that allows it to generate human-like responses to text-based queries. Additionally, ChatGPT is capable of completing tasks such as translation, summarization, and sentiment analysis. Its ability to learn from previous conversations and adapt its responses accordingly makes it an extremely powerful tool for a wide range of applications, including customer service, education, and healthcare. ChatGPT has had a significant impact on the field of natural language processing, making it easier for individuals and businesses to communicate with customers, patients, and clients, without the need for a human intermediary. This has led to significant cost savings for businesses and improved access to information for individuals. ChatGPT has also facilitated the development of more advanced chatbots and virtual assistants. Despite its impressive capabilities, ChatGPT still has some limitations, including its tendency to generate biased or offensive responses and its limitation to text-based conversations. However, the potential for ChatGPT and other advanced conversational AI is immense, with future versions expected to address many of the current limitations and integrate with other technologies such as machine learning and computer vision. Advanced conversational AI such as ChatGPT will likely continue to play an important role in the future of natural language processing, improving communication and access to information for individuals and businesses alike.'
chatGPT = 'ChatGPT is an advanced conversational AI developed by OpenAI, based on the GPT-3 architecture. It has a vast knowledge base and can generate human-like responses to text-based queries, as well as completing tasks such as translation, summarization, and sentiment analysis. ChatGPT has significant applications in various fields, including customer service, education, and healthcare. While it has some limitations, the potential for advanced conversational AI is immense, and it will likely continue to play an important role in the future of natural language processing.'
@app.post("/")
def summary(post:Post):
    #news_api = f'https://newsapi.org/v2/everything?q={post.topic}&pageSize={post.article_count}&apiKey={apikey}'
    #response = requests.get(news_api)
    #news = json.loads(response.content)
    results = {}
    #for article_info in news['articles']:
        #article = Article(article_info['url'])
        #article.download()
        #article.parse()
    ot = example
    result = {}
    result['article']=ot
    result['chatGPT']=chatGPT
    klsum={}
    klsum['summary']=kl(ot)
    # klsum['rouge']=rouge.get_scores(klsum['summary'],result['article'])[0]
    klsum['rouge']=scorer.score(chatGPT,klsum['summary'])
    klsum['score']=score(klsum['rouge'])
    result['klsum']=klsum
    print(result)
    lexrank={}
    lexrank['summary']=lex(ot)
    lexrank['rouge']=scorer.score(chatGPT,lexrank['summary'])
    lexrank['score']=score(lexrank['rouge'])
    result['lexrank']=lexrank
    print(result)
    lsa={}
    lsa['summary']=ls(ot)
    lsa['rouge']=scorer.score(chatGPT,lsa['summary'])
    lsa['score']=score(lsa['rouge'])
    result['lsa']=lsa
    print(result)
    luhn={}
    luhn['summary']=luh(ot)
    luhn['rouge']=scorer.score(chatGPT,luhn['summary'])
    luhn['score']=score(luhn['rouge'])
    result['luhn']=luhn
    print(result)
    bart={}
    bart['summary']=bar(ot)
    bart['rouge']=scorer.score(chatGPT,bart['summary'])
    bart['score']=score(bart['rouge'])
    result['bart']=bart
    print(result)
    pegasus={}
    pegasus['summary']=pegasu(ot)
    pegasus['rouge']=scorer.score(chatGPT,pegasus['summary'])
    pegasus['score']=score(pegasus['rouge'])
    result['pegasus']=pegasus
    print(result)
    # result['link'] = article_info['url']
    # result['img'] = article_info['urlToImage']
    # result['publishedAt'] = article_info['publishedAt']
    # result['author'] = article_info['author']
    # result['source'] = article_info['source']['name']
    # results[len(results)]=result
    return result

def kl(ot):
    from sumy.summarizers.kl import KLSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    kl_summarizer=KLSummarizer()
    summary_bundle= kl_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    print(1)
    return summary
def lex(ot):
    from sumy.summarizers.lex_rank import LexRankSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    lex_rank_summarizer = LexRankSummarizer()
    summary_bundle = lex_rank_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    print(2)
    return summary
def ls(ot):
    from sumy.summarizers.lsa import LsaSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    lsa_summarizer=LsaSummarizer()
    summary_bundle=lsa_summarizer(parser.document,sentences_count=3) 
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    print(3)
    return summary
def luh(ot):
    from sumy.summarizers.luhn import LuhnSummarizer
    parser=PlaintextParser.from_string(ot,Tokenizer('english'))
    luhn_summarizer=LuhnSummarizer()
    summary_bundle=luhn_summarizer(parser.document,sentences_count=3)
    summary = ''
    for sentence in summary_bundle:
        summary=summary+str(sentence)
    print(4)
    return summary
def bar(ot):
    summary_bundle=pipeline('summarization',model="philschmid/bart-large-cnn-samsum")
    print(5)
    summary = summary_bundle(ot[:4000])[0]['summary_text']
    print(6)
    return summary
def pegasu(ot):
    summary_bundle=pipeline('summarization',model="google/pegasus-cnn_dailymail")
    print(7)
    summary = summary_bundle(ot[:4000])[0]['summary_text'].replace('<n>','')
    print(8)
    return summary
def score(rouge):
    return (rouge['rouge1'][1]+rouge['rouge2'][1]+rouge['rougeL'][1])/3