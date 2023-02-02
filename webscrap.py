import requests
from bs4 import BeautifulSoup


res= requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.select('#score_34612759'))
# . for class
# '#' for id

print(soup.select('.score'))








