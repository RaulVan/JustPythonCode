__author__ = 'Eleven'
#
# encoding:UTF-8
# import urllib.request
#
# url = "http://www.baidu.com"
# data = urllib.request.urlopen(url).read()
# data = data.decode('UTF-8')
# print(data)

# print ("ddd")

#-*- encoding: utf-8 -*-
import urllib
import urllib.request
import http.cookiejar
import os
from bs4 import BeautifulSoup
import re

url_de_root="http://de.hujiang.com"
url_dw="http://de.hujiang.com/zt/dw"
rh = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36'}
page=""


def getHtmlPage(url):
    cookie = urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar())

    req = urllib.request.Request(url,headers=rh)
    page = urllib.request.urlopen(req).read()
    page = page.decode('utf-8')
    return page
urlDic=dict()
urlKeys=list()

def getListAtag(page):
    soup=BeautifulSoup(page)
    all_div=soup.find_all("div",class_="in_list_conent")
    #print (all_div)
    # return page
    for div in all_div:
        li_as=div.find_all('li',class_="unit")
        #print(li_as)
        for a in li_as:
            #print(a.find('a'))
            a=a.find('a')
            print( a.get_text()+(url_de_root+a.get('href')))
            #print("%s  %s  "%(a.get_text(),url_de_root+a.get('href')))
            #urlDic.update(a.get_text(),url_de_root+a.get('href'))
            #?????????¡ì?????????
            urlDic[a.get_text()]=url_de_root+a.get('href')
            urlKeys.append(a.get_text())
    return urlDic
      
        # page1= getHtmlPage(url_de_root+f_Url)
        # print(page1)
# ???¡§¡§?????¡§¡§?? div id="article_summary" class="article_summary"

def getPageConnect(htmlStr):
     soup=BeautifulSoup(htmlStr)



html=getHtmlPage(url_dw)
dictcc= getListAtag(html)

print(dictcc.get(urlKeys[0]))

#html=getHtmlPage(dictcc.items())
#print(html)
print("OK")



#TODO：先保存到文本。。。。然后上传



 



