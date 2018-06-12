# -*- coding: utf-8 -*
'''
填补空白单元格的蔬菜名称和批发市场名称
'''

import pandas as pd
from pandas import DataFrame
import xlrd
import xlwt


workbook = xlrd.open_workbook(r"D:\p\p001\1.1-1.10.xls")
print(workbook.sheet_names())

sheet1 = workbook.sheet_by_index(0)
print(sheet1.name, sheet1.nrows, sheet1.ncols)
sheet01 = workbook.sheet_by_name('Report')
print(sheet01.name, sheet1.nrows, sheet1.ncols)

nrows = sheet1.nrows
ncols = sheet1.ncols
