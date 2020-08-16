# -*- coding=utf-8 -*-

from butipicture.tools import *

file1 = open("image/html/186298068.html", "r", encoding="UTF-8")

content = file1.read()
image_urls = get_images_url(content)

print(image_urls)

file1.close()
