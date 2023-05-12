from newspaper import Article
import requests
import json
import xmltodict
from bs4 import BeautifulSoup

country = 'US'
response = requests.get(f'https://news.google.com/home?gl={country}')
soup = BeautifulSoup(response.text, 'html.parser')
feed = soup.find_all("a",{"class":"jKHa4e"})
href = str(feed[0].get('href')).replace('.','https://news.google.com')
response2 = requests.get(href)
soup2 = BeautifulSoup(response2.text, 'html.parser')
feed2 = soup2.find_all("a",{"class":"VDXfz"})
href2 = str(feed2[0].get('href')).replace('.','https://news.google.com')
print(len(feed2))
#response = requests.get(f'http://news.google.com/rss/search?q={topic}&gl={country}')
#response = requests.get(f'https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lnaXByNEJoSE1UWU1DWWhGSVp5Z0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen')
#news = json.loads(json.dumps(xmltodict.parse(response.content)))
"""
topic = 'Modi'
country = 'IN'
url = (news['rss']['channel']['item'][0]['link'])
article = Article(url)
article.download()
article.parse()
print((article.text))
article.nlp()
print(article.keywords)
print(article.summary)
"""