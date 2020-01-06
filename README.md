# py-demo-live-streaming

# dlts_dianbo.py 爬取网上的点播流
# dlts_zhibo.py 爬取网上的直播流，生成新的直播流

# 百度云播放器
http://cyberplayer.bcelive.com/demo/new/index.html
# hls点播
http://gcqq450f71eywn6bv7u.exp.bcevod.com/mda-hiup6h1qdymgf3fe/mda-hiup6h1qdymgf3fe.m3u8
# hls直播
http://cyberplayerplay.kaywang.cn/cyberplayer/demo201711-L1.m3u8
# CCTV高清
ivi.bupt.edu.cn/hls/cctv1hd.m3u8
http://ivi.bupt.edu.cn/hls/cctv1hd-1577808717000.ts

上面两个m3u8文件内容放在m3u8_files下：
点播时m3u8文件是固定的，该视频是6:07分钟。
http://gcqq450f71eywn6bv7u.exp.bcevod.com/mda-hiup6h1qdymgf3fe/mda-hiup6h1qdymgf3fe.m3u8.4.ts
单个文件是9秒。所以 40*9+7 = 6*60+7


直播时m3u8文件是变化的。
http://cyberplayerplay.kaywang.cn/cyberplayer/demo201711-L1-1577803636784.ts
http://ivi.bupt.edu.cn/hls/cctv1hd-1577808717000.ts

# 参考文章：

urllib简单爬取m3u8地址的所有ts文件并下载
https://blog.csdn.net/z564359805/article/details/81055321

Python爬虫——从流媒体网站获取的m3u8爬取视频 （点播）
https://blog.csdn.net/kingyuan666/article/details/90247526

Python实现自动录制虎牙直播
https://blog.csdn.net/jamkkils/article/details/87864222

可用直播流测试用
https://blog.csdn.net/csdndouniwan/article/details/89680407

# 思路
同步直播流的m3u8文件
循环读取最新m3u8文件，寻找未下载的ts文件,下载下来
只保留最新的20个ts文件

# 关于直播的参考文章

Mac直播服务器Nginx配置对HLS的支持
https://www.cnblogs.com/jys509/p/5653720.html
Mac上搭建直播服务器Nginx+rtmp
https://www.cnblogs.com/jys509/p/5649066.html


# 扩展
[FFmpeg] ffmpeg 常用命令
https://www.cnblogs.com/frost-yen/p/5848781.html

# 直播平台流媒体服务器搭建（Linux+Nginx+RTMP）
https://blog.csdn.net/EricZwz/article/details/84581409

# ffmpeg+nginx+rtmp+web实现视频直播网站
https://blog.csdn.net/fu_shuwu/article/details/89598311

# 怎样在vmix中进行直播推流？
https://www.gxqwkj.com/vmixkc/1695.html
windows中下载vmix20，使用基础版，先免费注册。
获得key，即可以使用
在mac中也可以下载OBS软件。

# [vmIx教程]vmix使用NDI功能输出操作说明  (旁边有相关推荐)
https://www.bilibili.com/video/av74051561

# 快速搭建自己的直播服务器，完成属于你直播服务
https://www.jianshu.com/p/f304b3d18713

# mac上虚拟机win10与主机网络互ping
https://www.jianshu.com/p/755bee85b2ff
这个关系到mac中的windows虚拟机中的vMix访问mac中的nginx的直播服务器

# Windows系统下ffmpeg+nginx搭建HLS服务器
https://www.jianshu.com/p/0c1f96a2cf49。

# Video.js使用教程
http://www.pianshen.com/article/6489340119/;jsessionid=E613F9DAE38668D1F4EB242A74A5A513

# Windows下实现ffmpeg+nginx+rtmp+hls实现直播推流拉流（低延时）
https://blog.csdn.net/u011925282/article/details/102580420

# rsync同步服务的总结(Linux与windows双向)
https://www.jianshu.com/p/bb9f53750b3e

# Windows下用FFmpeg+nginx+rtmp搭建直播环境_实现推流、拉流（超简单教程)
https://www.jianshu.com/p/eacfc0a9f2fd
