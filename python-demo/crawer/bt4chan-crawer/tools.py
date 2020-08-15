# -*- coding=utf-8 -*-
import os
import re
import urllib.request

"""
http spider tool
@author vvyun
"""


def get_html(url):
    """
    get url's html content
    :param url: http url
    :return : the content of url's html
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        data = response.read().decode("utf-8")
        return data
    except urllib.request.HTTPError:
        return ''
    except urllib.request.URLError:
        return ''


def save2file(filename, content):
    """
    save content to file
    :param filename: file's full name
    :param content: str
    """
    output = open(filename, "w+", encoding="utf8")
    output.write(content)
    output.close()


def get_catalogs(content):
    """
    get 4chan's catalog data
    :param content: 4chan's html content
    :return: catalogs
    """
    pattern = r"var\scatalog\s=(.*).var\sstyle_group"
    res = re.search(pattern, content, re.M | re.S)
    return res.group(1)


def get_images_url(content):
    """
    get img download url
    :param content: html content
    """
    pattern = r"a\shref=\"(//i.4cdn.org/.*?\.[j|p|g][p|n|i][g|f])\""
    res = re.findall(pattern, content)
    return res


def url_isuseful(url):
    """
    check url status
    :param url: url
    :return: number 0-ok 1|2|3-error
    """
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-agent", "Mozilla/49.0.2")]
    try:
        opener.open(url)
        return 0
    except urllib.request.HTTPError:
        return 1
    except urllib.request.URLError:
        return 2


def download_img(img_url, img_name):
    """
    download img
    :param img_url:
    :param img_name:
    :return:
    """
    try:
        if url_isuseful(img_url) < 1:
            urllib.request.urlretrieve(
                img_url, img_name
            )
    except Exception as e:
        raise e


def mkdir(path):
    """
    make a dir ,if is exists return false
    :param path: dir's name
    :return: file exists return false else return true
    """
    path = path.strip()
    path = path.rstrip("\\")

    exists = os.path.exists(path)
    if not exists:
        os.makedirs(path)
        return True
    else:
        return False
