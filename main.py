from bs4 import BeautifulSoup
import requests


# target html look --> https://nicepage.com/html-templates/preview/perform-programming-157182?device=desktop



"""
threat_post_news = requests.get('https://threatpost.com/category/vulnerabilities/').text
soup_tp_news = BeautifulSoup(threat_post_news, 'lxml')
tp_articles_s1 = soup_tp_news.find_all('article', class_="c-card c-card__image-top")
tp_articles_s2 = soup_tp_news.find_all('article', class_="c-card c-card--horizontal--half@md c-card--horizontal@lg c-card--horizontal--flat@md js-post-item")

card_links = []
for each in tp_articles_s1:
    # print(each)
    temp_tuple = (each.a['href'], each.h2.text)
    card_links.append(temp_tuple)

for each2 in tp_articles_s2:
    temp_tuple = (each2.a['href'], each2.h2.text)
    card_links.append(temp_tuple)

# for x in card_links:
    # print(x[0]) # href
    # print(x[1]) # alt text
"""


hackerNews = requests.get('https://thehackernews.com/').text
soup_hackerNews = BeautifulSoup(hackerNews, 'lxml')
stories = soup_hackerNews.find_all('a', class_="story-link")
print()

hackerNews_urls = []
for tag in stories:
    print(tag.get('href'))
    print(tag.h2.text)
    date = tag.find('div', {'class': 'item-label'}).text
    i = tag.find('span').text
    newDate = date.replace(i, '')
    print(newDate)
    del date



"""
cyberNews = requests.get('https://cybernews.com/').text
soup = BeautifulSoup(cyberNews, 'lxml')
articles = soup.find_all('article')
cells = soup.find_all('cells')
# print(articles)

cyber_news_links = []
for links in articles:
    # print(links.a['href'])
    if "https://cybernews.com/news" in links.a['href']:
        # print(links.a['href'])
        temp_tuple = links.a['href'], links.h3.text, links.span.text #links.span.text = grabs the date 
        cyber_news_links.append(temp_tuple)
        # print('news')
    elif "https://cybernews.com/security" in links.a['href']:
        # print(links.a['href'])
        temp_tuple2 = links.a['href'], links.h3.text
        cyber_news_links.append(temp_tuple2)
        # print('security')

for x in cyber_news_links:
    print(x)
"""

# EOF
