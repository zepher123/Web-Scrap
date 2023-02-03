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
        link1 = links[idx].get('href', None)
        points = int(votes[idx].getText().replace(' points', ''))
        print(idx)
        h.append({'title2': title, 'link2': link1})
    return(h)

create_custom_hacker_news(links, votes)

