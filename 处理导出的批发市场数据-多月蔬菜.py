import pandas as pd
docAddress = r"D:\Data\信息中心批发价格\网络导出\2019年1月蔬菜.xlsx"
df = pd.read_excel(docAddress, Sheet_name='Sheet1')
df.shape
df.head()
df.info()

#df = df.drop('类', axis=1)
#df = df.loc[df['类'] != '蔬菜']
df = df.loc[df['蔬菜'] != '果菜']
df = df.loc[df['蔬菜'] != '叶菜']
df = df.loc[df['蔬菜'] != '其它蔬菜']
df.info()

#df = df.loc[df['月份'] != '2019年']
#df = df.loc[df['月份'] != '2019年第1月']

df = df[~df['日期'].str.contains('第')]
df.info()
df = df[df['批发市场'].str.len() > 3]

#df = df.drop('月份', axis=1)
df.info()

writer = r"D:\Data\信息中心批发价格\网络导出\2019年1月蔬菜_cleaned.xlsx"
df.to_excel(writer, sheet_name='cleaned', index=False)
