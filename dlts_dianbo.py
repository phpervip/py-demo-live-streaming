#!/usr/bin/env python
# coding=utf-8
# 爬取m3u8地址的所有ts文件并下载

import os
import sys
import time
import datetime
import requests
import os,re
import time
import urllib.request
import ssl
from urllib.error import URLError
ssl._create_default_https_context = ssl._create_unverified_context

def writefile(path, filename, data, type):
    with open(path + filename, type)as f:
        f.write(data)
var = 1
count = 0
path = "a/video/"
begin_url = "http://gcqq450f71eywn6bv7u.exp.bcevod.com/mda-hiup6h1qdymgf3fe/"
url = "http://gcqq450f71eywn6bv7u.exp.bcevod.com/mda-hiup6h1qdymgf3fe/mda-hiup6h1qdymgf3fe.m3u8"
while var == 1:
    os.system('./delsomefiles.sh')
    print("while starting")
    print("The count is:")
    print(count)
    count=count+1
    print("--count--")
    print(count)
    print("download starting")
    # 将来需要拼接的每一个ts视频文件地址的开头
    length = len(begin_url)
    # m3u8地址,下载下来会看到很多个ts文件名字组成
    response = requests.get(url)
    all_content = response.text

    # 按照结尾的换行符进行切片操作
    file_line = all_content.split("\n")
    # 存储将来拼接的所有ts链接地址
    url_list = []
    header = {
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);'
    }
    open(path + 'success.log', "wb")
    open(path + 'new_video_db.m3u8', "wb")
    print(file_line)
    for index, line in enumerate(file_line):
        if "EXTINF" in line:
            writefile(path, 'new_video_db.m3u8', file_line[index] + '\n', 'a+')
            pd_url = begin_url + file_line[index + 1]  # 拼出ts片段的URL
            url_list.append(pd_url)
            file_name = file_line[index+1]
        else:
            writefile(path, 'new_video_db.m3u8', file_line[index] + '\n', 'a+')
    url_length = len(url_list)
    for i in range(len(url_list)):
        add_url = url_list[i]
        # 正则取出数字文件名字
        patt = re.compile(r'\d+')
        file_name = add_url.split("/")[-1]
        print()
        request = urllib.request.Request(add_url, headers=header)
        response = urllib.request.urlopen(request)
        html = response.read()
        result_file_name=url_list[i][length:]
        print("正在处理%s" % result_file_name, "共%s/%s项" % (i + 1, url_length))
        time.sleep(1)
        path = "a/video/"
        if (not os.path.exists(path)):
            os.makedirs(path)
        with open(path + result_file_name, "wb")as f:
            f.write(html)
