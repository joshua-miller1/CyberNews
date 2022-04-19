from django.shortcuts import render
from bs4 import BeautifulSoup
from .models import ThreatPostLinks
import requests

# Create your views here.
# request handler


def scrape_threat_post():
    threat_post_news = requests.get('https://threatpost.com/category/vulnerabilities/').text
    soup_tp_news = BeautifulSoup(threat_post_news, 'lxml')
    tp_articles_s1 = soup_tp_news.find_all('article', class_="c-card c-card__image-top")
    tp_articles_s2 = soup_tp_news.find_all('article',
                                           class_="c-card c-card--horizontal--half@md c-card--horizontal@lg c-card--horizontal--flat@md js-post-item")

    card_info = []
    for each in tp_articles_s1:
        # print(each)
        temp_tuple = (each.a['href'], each.h2.text)
        card_info.append(temp_tuple)

    for each2 in tp_articles_s2:
        temp_tuple = (each2.a['href'], each2.h2.text)
        card_info.append(temp_tuple)

    return card_info


def scrape_hacker_news():
    hacker_news = requests.get('https://thehackernews.com/').text
    soup_hacker_news = BeautifulSoup(hacker_news, 'lxml')
    stories = soup_hacker_news.find_all('a', class_="story-link")
    hacker_news_info = []
    for tag in stories:
        temp_tuple = (tag.get('href'), tag.h2.text)
        hacker_news_info.append(temp_tuple)
    return hacker_news_info


def scrape_cyber_news():
    cyber_news = requests.get('https://cybernews.com/').text
    soup = BeautifulSoup(cyber_news, 'lxml')
    articles = soup.find_all('article')

    temp = []
    for links in articles:
        if "https://cybernews.com/news" in links.a['href']:
            temp_tuple = links.a['href'], links.h3.text
            temp.append(temp_tuple)
        elif "https://cybernews.com/security" in links.a['href']:
            temp_tuple2 = links.a['href'], links.h3.text
            temp.append(temp_tuple2)

    cyber_news_info = []
    for x in temp:
        if x not in cyber_news_info:
            cyber_news_info.append(x)
    temp.clear()

    return cyber_news_info


def get_cyber_news_links(request):
    # pull data from db

    # pull cybernews.com links and add context dictionary
    cyber_news_info = []
    for x in scrape_cyber_news():
        cyber_news_info.append(x)
    # list_of_values = list_of_values

    hacker_news_info = []
    for x in scrape_hacker_news():
        hacker_news_info.append(x)

    threat_post_info = []
    for x in scrape_threat_post():
        threat_post_info.append(x)

    # context is scrape cyber news
    context = {}
    context['cyber_news_info'] = cyber_news_info
    context['hacker_news_info'] = hacker_news_info
    context['threat_post_info'] = threat_post_info
    return render(request, 'cyber_news.html', context)


# EOF
