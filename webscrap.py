import requests
from bs4 import BeautifulSoup


res= requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# . for class
# '#' for id

links = (soup.select('.titleline')) #learn css selectors
votes = (soup.select('.score'))

print(votes[0].get('id')) #get attribute id and it prints value as score










