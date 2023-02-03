import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# . for class
# '#' for id

links = (soup.select('.titleline'))  # learn css selectors
subtext = (soup.select('.subtext'))


# print(votes[0].get('id')) #get attribute id and it prints value as score


def create_custom_hacker_news(links, subtext):
    h = []
    for idx, item in enumerate(links):  # enumerate gives index
        title = links[idx].getText()
        link1 = links[idx].get('href', None)
        votes = (subtext[idx].select('.score'))

        if len(votes):

            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:


                h.append({'title2': title, 'link2': link1, 'points2': points})
    return (h)


pprint.pprint(create_custom_hacker_news(links, subtext))
