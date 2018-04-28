# -*- coding: utf-8 -*-
import requests
import json
import time
import os


headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'zh-CN,zh;q=0.9',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
'Accept-Encoding': 'gzip, deflate, br',
'Host': 'vjudge.net',
'method': 'POST',
'path': '/contest/data',
'authority': 'vjudge.net',
'cookie': 'SESSIONID=E9D642A8175DBDDDD06FB1AE838227B5',
'origin': 'https://vjudge.net',
'referer': 'https://vjudge.net/user',
'x-requested-with': 'XMLHttpRequest'
}
post_data = {
    'draw': '1',
    'columns[0][data]': '0',
    'columns[0][name]': '',
    'columns[0][searchable]': 'true',
    'columns[0][orderable]': 'false',
    'columns[0][search][value]':  '',
    'columns[0][search][regex]': 'false',
    'columns[1][data]': '1',
    'columns[1][name]': '',
    'columns[1][searchable]': 'true',
    'columns[1][orderable]': 'true',
    'columns[1][search][value]':  '',
    'columns[1][search][regex]': 'false',
    'columns[2][data]': '2',
    'columns[2][name]': '',
    'columns[2][searchable]': 'false',
    'columns[2][orderable]': 'false',
    'columns[2][search][value]': '',
    'columns[2][search][regex]': 'false',
    'columns[3][data]': '3',
    'columns[3][name]': '',
    'columns[3][searchable]': 'true',
    'columns[3][orderable]': 'true',
    'columns[3][search][value]': '',
    'columns[3][search][regex]': 'false',
    'columns[4][data]': '4',
    'columns[4][name]': '',
    'columns[4][searchable]': 'true',
    'columns[4][orderable]': 'true',
    'columns[4][search][value]': '',
    'columns[4][search][regex]': 'false',
    'columns[5][data]': '5',
    'columns[5][name]': '',
    'columns[5][searchable]': 'true',
    'columns[5][orderable]': 'true',
    'columns[5][search][value]': '',
    'columns[5][search][regex]': 'false',
    'columns[6][data]': '6',
    'columns[6][name]': '',
    'columns[6][searchable]': 'true',
    'columns[6][orderable]': 'false',
    'columns[6][search][value]': '',
    'columns[6][search][regex]': 'false',
    'order[0][column]': '5',
    'order[0][dir]': 'desc',
    'start': '0',
    'length': '100',
    'search[value]': '',
    'search[regex]': 'false',
    'OJId': 'All',
    'probNum': '',
    'title': '',
    'source': '',
    'category': 'all'
}

url = "https://vjudge.net/user/data"

def get_data():

    now_time = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    abspath = os.path.abspath('.')
    print(now_time)
    # 路径
    dir_path = str(abspath) + '\data\user'
    fpath = dir_path + '\\' + str(now_time) + '.txt'
    print(fpath)
    # 文件夹不存在，则创建
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    try:
        for i in range(1, 11):
            time.sleep(2)
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


if __name__ == "__main__":
    get_data()

