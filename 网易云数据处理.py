'''1.标题栏为:标题	日期	点赞数	播放量	评论数	分享数	时长	节目	爬取时间	平台
2.去除待处理表格中的 字段2
3.将点赞数中的'赞'去掉,并将字符串改为数组
4.去除播放量中的文字, 保留数自, 大于10的播放量需要 * 10000
5.将评论数与分析数设为0
6.将字段6中的时长改为秒数
7.节目 设置为表格名称'-'之前的内容
8.爬取时间设置为'2020-03-31'
9.平台设置为 '网易云音乐'
'''

import pandas as pd
docAddress = r"C:\Users\MaleBird\Desktop\日谈公园-网易云-待处理.xlsx"
df = pd.read_excel(
    docAddress,
    sheet_name='sheet1',
    header=None,
    names=["标题", "播放量", "点赞数", "日期", "时长"],
    usecols="B,D:G",
    skiprows=1)

df.info()
print(df.head())
