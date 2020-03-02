import requests
from bs4 import BeautifulSoup
from pprint import pprint

res1 = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup1 = BeautifulSoup(res1.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links1 = soup1.select('.storylink')
subtext1 = soup1.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')
# print(links)
# print(subtext)
megalink = links1 + links2
megasubtext = subtext1 + subtext2


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        # print(vote)
        if (len(vote)):
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                hn.append({'title': title, 'links': href, 'votes': points})
    return sort_stories_by_votes(hn)


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


pprint(create_custom_hn(megalink, megasubtext))
