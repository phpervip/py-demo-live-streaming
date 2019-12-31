#!/usr/bin/env python
# coding=utf-8
# 爬取m3u8地址的所有ts文件并下载

import os
import sys
import time
import datetime
import requests
import os
import time
import urllib.request
import ssl
from urllib.error import URLError

var = 1
count = 0
while var == 1:
    count = count+1
    print('-count-')
    print(count)
    time.sleep(3)
