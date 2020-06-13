import requests
import sys
import io
import re
import time
import random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

def getHtml(s):
    #登录后才能访问的网页
    #*里填你的独特的id
    url = 'https://www.douban.com/people/******/statuses?p='+s

    #浏览器登录后得到的cookie，也就是刚才复制的字符串
    cookie_str = r'your_cookie'

    #把cookie字符串处理成字典，以便接下来使用
    cookies = {}
    for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

    #设置请求头
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

    #在发送get请求时带上请求头和cookies
    resp = requests.get(url, headers = headers, cookies = cookies)
            
    print (resp.content.decode('utf-8'))
    return resp.content.decode('utf-8')

def filt(result):
    regix = r'<div class="bd sns">.*?<div class="status-saying">.*?<blockquote class=quote-clamp>.*?<p>(.*?)</p>.*?<div class="actions">.*?<span class="created_at" title=(.*?)>.*?'
    results = re.findall(regix,result,re.S)
    #your filepath to save data
    with open('your_file_path','a+') as f:
        for item in results:
            f.write(item[1]+"\n"+item[0]+"\n\n")

if __name__ == '__main__':
    for i in range (1,200):
        time.sleep(random.random())
        result = getHtml(str(i))
        filt(result)