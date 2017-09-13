import requests
r = requests.get('https://api.douban.com/v2/book/1291546')
data = r.json()
r.text#两者的区别是什么？
