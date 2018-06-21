# -*- coding: utf-8 -*
'''
填补空白单元格的蔬菜名称和批发市场名称
修改日期格式
'''

import xlrd
import xlwt
from xlutils.copy import copy

workbook = xlrd.open_workbook(r"D:\p\p001\1.1-1.10.xls")
print(workbook.sheet_names())

sheet1 = workbook.sheet_by_index(0)
print('index为0的sheet：', sheet1.name, sheet1.nrows, sheet1.ncols)
sheet01 = workbook.sheet_by_name('Report')
print('name为Report的sheet：', sheet01.name, sheet1.nrows, sheet1.ncols)


nrows = sheet1.nrows
ncols = sheet1.ncols

#copy已读取的文件
book = copy(workbook)
#获取名为Report的sheet
sheet2 = book.get_sheet('Report')

#在第11行添加标题栏
head = ['蔬菜','批发市场','日期','大宗价','最高价','最低价','交易量','产地']
for i in range(0,8):
    sheet2.row(10).write(i,head[i])
    print('正在修改第'+str(i)+'个标题栏')

#填补蔬菜栏的空白
tempVeg =''
for i in range(11, nrows):
    if sheet01.cell_value(i,0) is not "":
        print(i)
        tempVeg = sheet01.cell_value(i, 0)
        i += 1
    else:
        sheet2.write(i, 0, tempVeg)
        i += 1

#填补批发市场的空白
tempMarket =''
for i in range(11, nrows):
    if sheet01.cell_value(i,1) is not "":
        print(i)
        tempMarket = sheet01.cell_value(i, 1)
        i += 1
    else:
        sheet2.write(i, 1, tempMarket)
        i += 1
print('已完成填补批发市场')

#修改日期单元格
'''
datevalue = sheet01.cell_value(13, 2)
print(datevalue)
'''
for i in range(13, nrows):
    datevalue = sheet01.cell_value(i, 2)
    sheet2.write(i, 2, datevalue[9:])
    i += 1

#保存
book.save(r"D:\p\p001\201701_1.xls")
