# py-demo-live-streaming

# download_ts_dianbo.py 爬取网上的点播流
# download_ts_zhibo.py 爬取网上的直播流，生成新的直播流

# 百度云播放器
# http://cyberplayer.bcelive.com/demo/new/index.html
# hls点播
# http://gcqq450f71eywn6bv7u.exp.bcevod.com/mda-hiup6h1qdymgf3fe/mda-hiup6h1qdymgf3fe.m3u8
# hls直播
# http://cyberplayerplay.kaywang.cn/cyberplayer/demo201711-L1.m3u8
# CCTV高清
# ivi.bupt.edu.cn/hls/cctv1hd.m3u8
# http://ivi.bupt.edu.cn/hls/cctv1hd-1577808717000.ts

# 上面两个m3u8文件内容放在m3u8_files下：
# 点播时m3u8文件是固定的，该视频是6:07分钟。
# http://gcqq450f71eywn6bv7u.exp.bcevod.com/mda-hiup6h1qdymgf3fe/mda-hiup6h1qdymgf3fe.m3u8.4.ts
# 单个文件是9秒。所以 40*9+7 = 6*60+7


# 直播时m3u8文件是变化的。
# http://cyberplayerplay.kaywang.cn/cyberplayer/demo201711-L1-1577803636784.ts

# http://ivi.bupt.edu.cn/hls/cctv1hd-1577808717000.ts

# 参考文章：

# urllib简单爬取m3u8地址的所有ts文件并下载
# https://blog.csdn.net/z564359805/article/details/81055321

# Python爬虫——从流媒体网站获取的m3u8爬取视频 （点播）
# https://blog.csdn.net/kingyuan666/article/details/90247526

# Python实现自动录制虎牙直播
# https://blog.csdn.net/jamkkils/article/details/87864222

# 可用直播流测试用
# https://blog.csdn.net/csdndouniwan/article/details/89680407

# 思路
# 同步直播流的m3u8文件
# 循环读取最新m3u8文件，寻找未下载的ts文件,下载下来
# 只保留最新的40个ts文件

# 关于直播的参考文章

# Mac直播服务器Nginx配置对HLS的支持
# https://www.cnblogs.com/jys509/p/5653720.html
# Mac上搭建直播服务器Nginx+rtmp
# https://www.cnblogs.com/jys509/p/5649066.html
