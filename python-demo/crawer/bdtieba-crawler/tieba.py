# -*- coding=utf-8 -*-
"""
贴吧爬虫
author yun
"""
from fourchan.tools import *

cfile = open('config.ini')
a = cfile.read()

# url
urlindexbase = str(a).split('\n')[0].split('=')[1]

# https://tieba.baidu.com/f?kw=%E9%AD%94%E6%B3%95%E7%A6%81%E4%B9%A6%E7%9B%AE%E5%BD%95&ie=utf-8&pn=50
# https://tieba.baidu.com/f?kw=%E9%AD%94%E6%B3%95%E7%A6%81%E4%B9%A6%E7%9B%AE%E5%BD%95&ie=utf-8&pn=100
# https://tieba.baidu.com/f?kw=%E9%AD%94%E6%B3%95%E7%A6%81%E4%B9%A6%E7%9B%AE%E5%BD%95&ie=utf-8&pn=150

# 获取首页html内容
content = get_html(urlindexbase)

# 保存首页html内容到本地
indexfilename = "index_spider.html"
save2file(indexfilename, content)

# 正则提取所有帖子连接
rcmp = re.compile(r'<a rel="noreferrer" href="(.p.*?)" title="(.*?)" target="_blank" class=".*?">.*?<.a>',
                  re.S | re.I)

# 获取目录信息
catalog_index = rcmp.findall(content)

# 保存链接信息到本地
filenamecatlog = "catalog.txt"

file_catlog = open(filenamecatlog, 'a', encoding='utf8')

for raw in catalog_index:
    file_catlog.write('url:' + raw[0] + '\t\ttitle:' + raw[1] + '\n')

file_catlog.close()

urlthreadbase = 'https://tieba.baidu.com'

# 循环获取每个thread的所有图片
for thread_url in catalog_index:
    print(urlthreadbase + thread_url[0])
    # 获取thread页面html内容
    content_thread = get_html(urlthreadbase + thread_url[0])

    # 保存路径
    thread_save_basepath = "thread" + thread_url[0] + "/"

    # 创建保存目录
    mkdir(thread_save_basepath)
    save2file(thread_save_basepath + 'cnt.html', content_thread)
