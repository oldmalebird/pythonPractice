import pandas as pd
docAddress = r"D:\Data\信息中心批发价格\网络导出\2019年瓜菜汇总.xlsx"
df = pd.read_excel(docAddress, sheet_name='cleaned')
df.shape
df.head()
df.info()

#向下填充蔬菜、省、批发市场、月份列
df['蔬菜'] = df['蔬菜'].fillna(method='ffill')
df['省'] = df['省'].fillna(method='ffill')
df['批发市场'] = df['批发市场'].fillna(method='ffill')
df['月份'] = df['月份'].fillna(method='ffill')

#删除不需要的汇总行
df = df.loc[df['蔬菜'] != '瓜类']

#删除2020年的汇总数
#df = df.loc[df['月份'] != '2020年']
#df = df.loc[df['月份'] != '2020年第3月']
#df = df.loc[df['月份'] != '2020年第3月']

#删除2019年的汇总数
df = df.loc[df['月份'] != '2019年']

df = df[~df['日期'].str.contains('第')]
#如果此列因为有空值导致出错，df = df[~df['日期'].str.contains('第',na=False)]

#df = df[df['a'].str.len() > 3]
#df = df[df.a.str.len() > 3]
df = df[~(df['批发市场'].str.len() < 4)]

df = df.drop('月份', axis=1)
df.info()

writer = r"D:\Data\信息中心批发价格\网络导出\2019年瓜菜汇总_cleaned.xlsx"
df.to_excel(writer, sheet_name='cleaned', index=False)
