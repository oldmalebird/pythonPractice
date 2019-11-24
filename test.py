#汇总全国价格
import pandas as pd

df = pd.read_excel(
    r"D:\中国蔬菜协会data\生产者价格\[2019-1-1—2019-11-23]白菜信息速采(部省)汇总查询.xls")
#print(df.describe())
print(df.head())
#print(df.describe())
print(df.tail())
