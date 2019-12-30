#!/usr/bin/env python
# coding=utf-8
# 爬取m3u8地址的所有ts文件并下载

import os
import sys
import requests
import os
import time
import urllib.request
import ssl
#from urllib.request import Request, urlopen
from urllib.error import URLError
ssl._create_default_https_context = ssl._create_unverified_context

print("starting")
# 将来需要拼接的每一个ts视频文件地址的开头
begin_url = "http://hls.ciguang.tv/hdtv/"
length = len(begin_url)
# m3u8地址,下载下来会看到很多个ts文件名字组成
url = "http://hls.ciguang.tv/hdtv/video.m3u8?auth_key=1541992664-0-0-6cd3cfc720d8e82ba7d589ce7386717d"
response = requests.get(url)
#print("--response--")
#print(response)
all_content = response.text
#print("--all_content--")
#print(all_content)
# 按照结尾的换行符进行切片操作
file_line = all_content.split("\n")
#print("--file_line--")
#print(file_line)

# 存储将来拼接的所有ts链接地址
url_list = []
path = "A/video/"
header = {
    'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);'
}
for index, line in enumerate(file_line):
    #print("--index--")
    #print(index)
    #print("--line--")
    #print(line)
    if "EXTINF" in line:
        pd_url = begin_url + file_line[index + 1]  # 拼出ts片段的URL
        #print("--pd_url--")
        #print(pd_url)
        url_list.append(pd_url)
        file_name = file_line[index+1][21:-57]
        #print("--file_name--")
        #print(file_name)
#print("--url_list--")
#print(url_list)
for i in range(len(url_list)):
    #print("--i--")
    #print(i)
    add_url = url_list[i]
    #print("--add_url--")
    #print(add_url)
    request = urllib.request.Request(add_url, headers=header)
    #response = urllib.request.urlopen(request)

    #print("--response--")
    #print(response)

    # 重试30次
    attempts = 0
    success = False
    while attempts < 30 and not success:
        try:
            response = urllib.request.urlopen(request)
        except HTTPError as e:
            print("server couldn't fulfill the request.")
            print("Error code: ", e.code)
            attempts += 1
        except URLError as e:
            print("We failed to reach a server.")
            print("Reason: ", e.reason)
            attempts += 1
        else:
            print("good!  ", add_url[length:][21:-57])
            success = True

    html = response.read()
    file_name = url_list[i][length:][21:-57]
    # print(add_url)
    # print(file_name)

    time.sleep(2)
    # path = "A/video/"
    if (not os.path.exists(path)):
        os.makedirs(path)
    with open(path + file_name, "wb")as f:
        f.write(html)

print("ts保存地址:")
print(path)
# os.chdir(path)
# cmd = "cat *.ts > all.ts"
# os.system(cmd)
# os.system("mv all.ts new.mp4")



# 本文参考自 https://blog.csdn.net/z564359805/article/details/81055321


