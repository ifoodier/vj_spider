# -*- coding: utf-8 -*-
import requests
import bs4
from bs4 import BeautifulSoup as bs
import json
import lxml
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()    # 产生异常信息
        r.encoding = r.apparent_encoding
        print(r.json())
        return r.text
    except:
        return "网页获取错误"
    return ""

def fillUnivList(ulist, html):
    soup = bs(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')  # tds = tr.find_all('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{4}^10}\t{2:{4}^10}\t{3:^10}"
    print(tplt.format("排名", "学校名称", "省市", "分数", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], u[3], chr(12288)))

def main():
    uinfo = []
    url = "https://vjudge.net/comment/thread?path=error&t=1524644989968.5"
    html = getHTMLText(url)
    print(html)
    # fillUnivList(uinfo, html)
    # printUnivList(uinfo, 100)

main()


