import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# . for class
# '#' for id

links = (soup.select('.titleline'))  # learn css selectors
votes = (soup.select('.score'))



# print(votes[0].get('id')) #get attribute id and it prints value as score


def create_custom_hacker_news(links, votes):
    h = []
    for idx, item in enumerate(links): #enumerate gives index
        title = links[idx].getText()

        h.append(title)
    return(h)

print(create_custom_hacker_news(links, votes))

