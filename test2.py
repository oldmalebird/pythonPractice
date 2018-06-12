# -*- coding: utf-8 -*
import pandas as pd
from pandas import DataFrame



df = pd.DataFrame(pd.read_excel(r"D:\p\p001\test.xlsx"))
print(df.dtypes)
print(df['b1'].dtypes)
head = ['蔬菜','批发市场','日期','大宗价','最高价','最低价','交易量','产地']
head1 = ['a','b','c','d','e','f','g','h']
