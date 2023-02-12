import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# . for class
# '#' for id

links = (soup.select('.titleline'))  # learn css selectors
subtext = (soup.select('.subtext'))
subtext2 = (soup.select('.subtext'))
links2 = (soup2.select('.titleline'))
megalinks = links + links2
megasubtext = subtext + subtext2


# print(votes[0].get('id')) #get attribute id and it prints value as score


def sort_by_votes(hlist):
    return sorted(hlist, key=lambda k: k['points'], reverse=True)

def create_custom_hacker_news(links, subtext):
    h = []
    for idx, item in enumerate(links):  # enumerate gives index
        title = links[idx].getText()
        link1 = links[idx].get('href', None)
        votes = (subtext[idx].select('.score'))

        if len(votes):

            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                h.append({'title': title, 'link': link1, 'points': points})
    return sort_by_votes(h)



pprint.pprint(create_custom_hacker_news(megalinks, megasubtext))



