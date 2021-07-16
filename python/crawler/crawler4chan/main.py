# -*- coding=utf-8 -*-
# author vvyun
import json

from butipicture.tools import *

url = 'https://boards.4chan.org/'

# thread name
thread_names = ["a", "e", "ck"]
# default a（animate)
thread_name = thread_names[0]

url_catalogs = url + thread_name + "/catalog"
baseurl_threads = url + thread_name + "/thread/"

# get catalog html content
content = get_html(url_catalogs)

# save catalog html
# filename = "image/content_4chan_a.html"
# savestr2file(filename, content)

# get catalog
catalog_index = get_catalogs(content)

# save catalog
# filenameimg = "image/catalog_4chan.json"
# savestr2file(filenameimg, catalog_index)

# get thread's url list
thread_urls = json.loads(catalog_index)["threads"]

for thread_url in thread_urls:
    print(baseurl_threads + thread_url)
    # get thread html
    content_thread = get_html(baseurl_threads + thread_url)
    # save thread html
    # filename = "image/html/" + thread_url + ".html"
    # savestr2file(filename, content_thread)

    # get thread's img download url
    image_urls = get_images_url(content_thread)
    # img save path
    img_save_basepath = "image/data/" + thread_url + "/"
    # make dir
    mkdir(img_save_basepath)
    for image_url in image_urls:
        # url too long
        if len(image_url) > 50:
            continue
        # download img
        img_download_url = "https:" + image_url
        print(img_download_url)
        download_img(img_download_url, img_save_basepath + image_url.replace('/', ''))
