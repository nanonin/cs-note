# -*- coding=utf-8 -*-
import re

from butipicture import tools

file_r = open("index_spider.html", "r", encoding="utf8")
html_content = file_r.read()
file_r.close()
print(html_content)
# <a rel="noreferrer" href="/p/6212474621" title="我觉得御坂妹妹的计算力可能真的等于美琴" target="_blank" class="j_th_tit
# ">我觉得御坂妹妹的计算力可能真的等于美琴</a>
rcmp = re.compile(r'<a rel="noreferrer" href="(.p.*?)" title="(.*?)" target="_blank" class=".*?">.*?<.a>', re.S | re.I)
res = rcmp.findall(html_content)
print(res)

file_r1 = open("thread/p/5996030231/cnt.html", "r", encoding="utf8")
html_content1 = file_r1.read()
file_r1.close()

# <img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=b43148f1c6fcc3ceb4c0c93ba244d6b7
# /96edc62a6059252d270bd9d73a9b033b5ab5b9de.jpg" size="84889" changedsize="true" width="560" height="840">
rcmp2 = re.compile(
    r'<img class="BDE_Image" src="(https:..imgsa.baidu.com.*?)" size=".*?" .*?>',
    re.S | re.I)
imgurl = rcmp2.findall(html_content1)

# 下载图片
for imd in imgurl:
    print(imd)
    tools.download_img(imd, './')
