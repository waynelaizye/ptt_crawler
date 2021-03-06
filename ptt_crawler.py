# -*- coding: utf-8 -*-
"""
Usage: 
    Give the words to be crawled in a txt (one word each row) and set "file_name"
    It can also search multiple words for one term by giving json file and setting "is_list" to False
    ex: {
            'TV': ['television', 'TV' , .....]
        }

@author: Wayne
"""
# Params
file_name = 'test.txt' # Specify the text file that contains the keywords to be crawled
board = ['Bank_Service', 'Gossiping', 'Finance', 'Stock'] # Give the list of boards to be crawled
data_after = '2020/04/01' # Set a starting date of posts (ex: '2020/07/20')
save_path = 'fubon' # The directory name of the output
pages_to_crawl_each_word = 10 # The maximum pages to be crawled each word
is_list = True
# True if the text file is one word each row.
# False if need multiple keywords for one topic, (ex: { 'TV': ['television', 'TV' , .....] })


import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import json
import os
import time

mon = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',\
       'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

def read_list():
    print('Reading', file_name)
    word_list = []
    with open(file_name, encoding = 'utf8') as f:
        ff = f.read().splitlines()
    for line in ff:
        word_list.append(line.split(',')) 
    print('Total', len(word_list), 'lines')
    return word_list

def read_json():
    print('Reading', file_name)
    with open(file_name, encoding = 'utf8') as f:
        data = json.load(f)
    return data

def crawl(word, board = ['Gossiping'], data_after = '2020/01/01'):
    """
    Reads single word to be crawled as input.
    """
    keyword = quote(word.encode('utf8'))
    articles = []
    for b in board:
        page = 1
        while page < pages_to_crawl_each_word:
            url = 'https://www.ptt.cc/bbs/' + b + '/search?page=' + str(page) + '&q=' + keyword
            if b =='Gossiping':
                res = requests.get(url, cookies={'over18': '1'})
            else:
                res = requests.get(url)
            if res.status_code != 200:
                break
            soup = BeautifulSoup(res.content, "html.parser")
            headline = soup.findAll("div", {"class": "r-ent"})
            if headline == None:
                break
            for h in headline:
                try:
                    dic = {'title':h.find("div", {"class": "title"}).text[:-1].split(']')[1][1:]}
    #                    'time':h.find("div", {"class": "date"}).text[1:]}
                except:
                    dic = {'title':h.find("div", {"class": "title"}).text[:-1]}
                try:
                    url2 = 'https://www.ptt.cc' + h.a.get('href')
                except:
                    continue
                if b =='Gossiping':
                    res2 = requests.get(url2, cookies={'over18': '1'})
                else:
                    res2 = requests.get(url2)
                soup2 = BeautifulSoup(res2.content, "html.parser")
                try:
                    date = soup2.findAll("span",{'class':"article-meta-value"})[-1].text.split()
                    if len(date[2]) == 1: 
                        date = date[4] + '/' + mon[date[1]] + '/0' + date[2]
                    else:
                        date = date[4] + '/' + mon[date[1]] + '/' + date[2]
                    if date < data_after:
                        break
                    dic['date'] = date
                    dic['content'] = ' '.join(soup2.find(id="main-content").text.split('--\n※')[0].split('\n')[1:])
                    dic['comment'] = []
                    comment = soup2.findAll("div", {"class": "push"})
                    for c in comment:
                        if c.find("span",{'class':"hl push-tag"}) == None:
                            dic['comment'].append({'push':c.find("span",{'class':"f1 hl push-tag"}).text,\
                                                   'text':c.find("span",{'class':"f3 push-content"}).text[2:]})
                        else:
                            dic['comment'].append({'push':c.find("span",{'class':"hl push-tag"}).text,\
                                                   'text':c.find("span",{'class':"f3 push-content"}).text[2:]})
                except:
                    print('Error with', url2)
                articles.append(dic)
            page += 1
    return articles

def save_data(articles, word, save_path):
    word = word.replace(" ", "_")
    word = word.replace("/", "")
    print('file name = {0}'.format(word))
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file = os.path.join(os.getcwd(),save_path, word + ".json")

    # save to json....
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

if __name__== "__main__":
#    word_list = read_list()
    print("This is ptt crawler")
    print('file = {0}, path = {1}'.format(file_name, save_path))
    if is_list:
        word_list = read_list()
        for words in word_list:
            articles = []
            name = words[0]
            for word in words:
                articles += crawl(word, board)
            save_data(articles, name, save_path)
    else:
        word_dic = read_json()
        for name in word_dic:
            articles = []
            for word in word_dic[name]:
                articles += crawl(word, board)
            save_data(articles, name, save_path)


