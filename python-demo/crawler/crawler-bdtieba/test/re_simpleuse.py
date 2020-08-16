import re

file_r1 = open("../thread/p/5996030231/cnt.html", "r", encoding="utf8")
html_content1 = file_r1.read()
file_r1.close()

# 获取title
rcmp2 = re.compile(
    r'<title>(.*?)<.title>',
    re.S | re.I)

titles = rcmp2.findall(html_content1)

print(titles[0])

# 获取
# <div id="post_content_.*?" class="d_post_content j_d_post_content " style="display:;">(.*?)</div>
rcmp3 = re.compile(
    r'<div id="post_content_.*?" class="d_post_content j_d_post_content " style="display:;">(.*?)</div>',
    re.S | re.I)
print(rcmp3.findall(html_content1))