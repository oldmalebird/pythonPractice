import requests
r = requests.get('https://api.douban.com/v2/book/1291546')
data = r.json()
r.text#两者的区别是什么？
r1 = requests.get('https://api.douban.com/v2/movie/subject/1764796')
r2 = requests.get('https://developers.douban.com/wiki/?title=movie_v2')#为什么老师提供的参考url跟豆瓣api不一样？


r3 = requests.get('https://api.douban.com/v2/movie/subject/1292224')
# 1292720, 1292052, 1295644, 1291546
data3 = r.json()
print(data['title'], data['rating']['average'])
