# -*- coding: utf-8 -*-
import requests
import json
import time
import os
import sys

url = "https://vjudge.net/contest/data"

headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'zh-CN,zh;q=0.9',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Accept-Encoding': 'gzip, deflate, br',
'Host': 'vjudge.net',
'method': 'POST',
'path': '/contest/data',
'authority': 'vjudge.net',
'cookie': 'JSESSIONID=A0FB89167B25513BE9C89FFE313B031A',
'origin': 'https://vjudge.net',
'referer': 'https://vjudge.net/contest',
'x-requested-with': 'XMLHttpRequest'
}

post_data = {
    'draw': '1',
    'columns[0][data]': 'function',
    'columns[0][name]': '',
    'columns[0][searchable]': 'true',
    'columns[0][orderable]': 'false',
    'columns[0][search][value]':  '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': 'function',
    'columns[1][name]': '',
    'columns[1][searchable]': 'true',
    'columns[1][orderable]': 'true',
    'columns[1][search][value]':  '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': 'function',
    'columns[2][name]': '',
    'columns[2][searchable]': 'false',
    'columns[2][orderable]': 'false',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': 'function',
    'columns[3][name]': '',
    'columns[3][searchable]': 'true',
    'columns[3][orderable]': 'true',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'columns[4][data]': 'function',
    'columns[4][name]': '',
    'columns[4][searchable]': 'true',
    'columns[4][orderable]': 'true',
    'columns[4][search][value]': '',
    'columns[4][search][regex]': 'false',
    'columns[5][data]': 'function',
    'columns[5][name]': '',
    'columns[5][searchable]': 'true',
    'columns[5][orderable]': 'true',
    'columns[5][search][value]': '',
    'columns[5][search][regex]': 'false',
    'columns[6][data]': 'function',
    'columns[6][name]': '',
    'columns[6][searchable]': 'true',
    'columns[6][orderable]': 'false',
    'columns[6][search][value]': '',
    'columns[6][search][regex]': 'false',
    'order[0][column]': '0',
    'order[0][dir]': 'desc',
    'start': '0',
    'length': '20',
    'search[value]': '',
    'search[regex]': 'false',
    'OJId': 'All',
    'probNum': '',
    'title': '',
    'source': '',
    'category': 'all',
    'owner': '',
    'running': '0'
}

def get_data():

    now_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    abspath = os.path.abspath('.')
    print(now_time)
    fpath = str(abspath) + '\data\\' + str(now_time) + '.txt'

    # try:
    #     with open(fpath, 'a', encoding='utf-8') as f:
    #         f.write('{')
    # except:
    #     print("写入数据异常")
    try:
        for i in range(1, 112846):
            time.sleep(2)
            print("Page: " + i)
            post_data['draw'] = str(i)
            post_data['start'] = str((i-1)*20)
            response = requests.post(url, data=post_data, headers=headers)
            js_dic = json.loads(response.text)
            js_list = js_dic["data"]

            for li in range(len(js_list)):
                print(js_list[li])
                try:
                    with open(fpath, 'a', encoding='utf-8') as f:
                        f.write(str(js_list[li]))
                        f.write(', ')
                except:
                    print("写入数据异常")
    except:
        if os.path.exists(fpath):
            os.remove(fpath)
        print("获取数据异常")

    # try:
    #     with open(fpath, 'a', encoding='utf-8') as f:
    #         f.write('}')
    # except:
    #     print("写入数据异常")

if __name__ == "__main__":
    get_data()

