from cgitb import text
import requests
import re

url = 'https://n.news.naver.com/mnews/article/015/0004695776?sid=101'

res = requests.get(url)
text = res.text

regex = re.compile('<.+?>')
tag = regex.findall(text)


for t in tag :
    text = text.replace(t, '')

print(text)