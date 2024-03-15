import requests
from lxml import html

# 弹幕列表
# https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid=784413464&pid=686287727&segment_index=1

# 评论列表
# https://api.bilibili.com/x/v2/reply/main?csrf=66d7ebc4fa296c78f19693e7af9276ed&mode=3&next=0&oid=686287727&plat=1&seek_rpid=&type=1
url = "https://www.bilibili.com/video/BV1LU4y1q7X4"

request_header = {
    "User-Agent":""
}

def a():
    result = requests.get(url, headers=request_header)
    content = result.content

    ##2. 4.25以上版本使用etree：
    etree = html.etree  # 获取etree
    x = etree.HTML(content)  # 获取xpath对象


if __name__ == '__main__':
    a()