# -*- coding: utf-8 -*
'''
遍历文件夹中的文件
'''

import os
dir = r"C:\Users\MaleBird\Desktop\批发价格（2011年至2017年）\2017\待处理"
dirs = os.listdir(dir)
'''for dirc in dirs:
    print(dirc)
'''
print(dirs)
print(len(dirs))

newdir = r"C:\Users\MaleBird\Desktop\批发价格（2011年至2017年）\2017\已处理"
newdirs = ['201701_1', '201701_2','201701_3','201702_1','201702_2', '201702_3', '201703_1', '201703_2', '201703_3',	'201704_1',	'201704_2',	'201704_3', '201705_1',	'201705_2', '201705_3', '201706_1', '201706_2',	'201706_3', 	'201707_1',	'201707_2',	'201707_3',	'201708_1', '201708_2',	'201708_3', '201709_1']
print(newdirs)
print(len(newdirs))


'''
对待处理的25个文件进行以下操作并保存为新文件
填补空白单元格的蔬菜名称和批发市场名称
修改日期格式
'''
import xlrd
import xlwt
from xlutils.copy import copy

workbookpath = dir + r'\\' + dirs[0]
print(workbookpath)
workbookOrigin = xlrd.open_workbook(workbookpath) #地址含中文可能有问题

print(workbookOrigin)
sheetOrigin = workbookOrigin.sheet_by_name('Report')
nrows = sheet1.nrows
workbookNew = copy(workbookOrigin)   #copy已读取的文件
sheetNew = workbookNew.get_sheet('Report')   #获取名为Report的sheet
#在第11行添加标题栏
head = ['蔬菜','批发市场','日期','大宗价','最高价','最低价','交易量','产地']
for j in range(8):
    sheet2.row(10).write(i,head[i])
#填补蔬菜栏的空白
