#!/usr/bin/env python
# coding=utf-8
# 爬取m3u8地址的所有ts文件并下载

import os
import sys
import time
import datetime
import urllib.request
import requests
import os
import ssl
from urllib.error import URLError
ssl._create_default_https_context = ssl._create_unverified_context

def writefile(path, filename, data, type):
    with open(path + filename, type)as f:
        f.write(data)

# 'A/video/success.log'
def hasfile(filepath,filename):
    res = 0
    with open(filepath, 'r') as foo:
        for line in foo.readlines():
            if file_name in line:
                print(file_name + '-已下载过，跳过-')
                res = 1
            break
    return res
path = "A/video/"
open(path + 'success.log', "wb")
open(path + 'update.log', "wb")
open(path + 'error.log', "wb")

var = 1
count = 0
while var == 1:
    # 中央电视台的直播流
    # begin_url = "http://ivi.bupt.edu.cn/hls/"
    # url = "http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8"

    # 本地搭建的直播流
    begin_url = "http://localhost/hls/"
    url = "http://localhost/hls/movie.m3u8"

    os.system('./delsomefiles.sh')
    #print("while starting")
    open(path + 'new_video_zb.m3u8', "wb")
    # print("The count is:")
    # print(count)
    count = count + 1
    print("--count--")
    print(count)
    # print("download starting")
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
    # print(file_line)
    for index, line in enumerate(file_line):
        if "EXTINF" in line:
            writefile(path, 'new_video_zb.m3u8', file_line[index] + '\n', 'a+')
            pd_url = begin_url + file_line[index + 1]  # 拼出ts片段的URL
            url_list.append(pd_url)
            file_name = file_line[index + 1]
        else:
            writefile(path, 'new_video_zb.m3u8', file_line[index] + '\n', 'a+')
    url_length = len(url_list)
    # print(url_list)
    for i in range(len(url_list)):
        add_url = url_list[i]
        file_name = url_list[i][length:]
        # print('-file_name-')
        # print(file_name)
        if(os.path.exists(path+file_name)):
            # print(file_name+'已存在')
            a = 1
        else:
            # print(file_name + '开始下载...')
            request = urllib.request.Request(add_url, headers=header)
            # print(request)
            # 重试30次
            attempts = 0
            success = False
            while attempts < 30 and not success:
                try:
                    response = urllib.request.urlopen(request)
                except:
                    print("We failed to reach a server. ")
                    print("retrying ... ")
                    attempts += 1
                    writefile(path, 'error.log', add_url[length:] + '\n', 'a+')
                else:
                    # print("good!  ", add_url[length:])
                    print(file_name + '下载完成...')
                    success = True
                    writefile(path, 'success.log', add_url[length:] + '\n', 'a+')

            html = response.read()
            file_name = url_list[i][length:]
            # time.sleep(1)
            # print(path + file_name)
            if (not os.path.exists(path)):
                os.makedirs(path)
            with open(path + file_name, "wb")as f:
                f.write(html)
    # print('download end')
    os.system('cp -f A/video/new_video_zb.m3u8 A/video/video_zb.m3u8')
    print('A/video/video_zb.m3u8 is update!')
    time.sleep(3)
    # writefile(path, 'error.log', '.' + '\n', 'a+')
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    writefile(path, 'update.log', t + '\n', 'w')

    # 用VCL打开 localhost/py-demo/A/video/video_zb.m3u8
