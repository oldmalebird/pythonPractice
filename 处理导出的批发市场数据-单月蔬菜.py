import pandas as pd
docAddress = r"D:\Data\信息中心批发价格\网络导出\2019年3月蔬菜.xlsx"
df = pd.read_excel(docAddress, sheet_name='Sheet1')
df.shape
df.head()
df.info()

#向下填充蔬菜、省、批发市场、月份列
#df['A'] = df['A'].fillna(method='ffill')
df['蔬菜'] = df['蔬菜'].fillna(method='ffill')
df['省'] = df['省'].fillna(method='ffill')
df['批发市场'] = df['批发市场'].fillna(method='ffill')
#df['日期'] = df['日期'].fillna(method='ffill')

#删除不需要的汇总蔬菜行
df = df.loc[df['蔬菜'] != '果菜']
df = df.loc[df['蔬菜'] != '叶菜']
df = df.loc[df['蔬菜'] != '其它蔬菜']

#删除单月的汇总数
df = df[~df['日期'].str.contains('第')]
#如果此列因为有空值导致出错，df = df[~df['日期'].str.contains('第',na=False)]

#删除批发市场列的省份汇总
#df = df[df['a'].str.len() > 3]
#df = df[df.a.str.len() > 3]
df = df[~(df['批发市场'].str.len() < 4)]

df.info()

writer = r"D:\Data\信息中心批发价格\网络导出\2019年3月蔬菜_cleaned.xlsx"
df.to_excel(writer, sheet_name='cleaned', index=False)
