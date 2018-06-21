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
newdirs = ['201701_1.xls ', '201701_2.xls ', '201701_3.xls ', '201702_1.xls ', '201702_2.xls ', '201702_3.xls ', '201703_1.xls ', '201703_2.xls ', '201703_3.xls ', '201704_1.xls ', '201704_2.xls ', '201704_3.xls ', '201705_1.xls ', '201705_2.xls ', '201705_3.xls ', '201706_1.xls ', '201706_2.xls ', '201706_3.xls ', '201707_1.xls ', '201707_2.xls ', '201707_3.xls ', '201708_1.xls ', '201708_2.xls ', '201708_3.xls', '201709_1.xls']
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

for i in range(len(dirs)):
    print(i)


for i in range(len(dir)):
    workbookpath = dir + r'\\' + dirs[i]
    workbookOrigin = xlrd.open_workbook(workbookpath) #地址含中文可能有问题
    sheetOrigin = workbookOrigin.sheet_by_name('Report')
    nrows = sheetOrigin.nrows
    workbookNew = copy(workbookOrigin)   #copy已读取的文件
    sheetNew = workbookNew.get_sheet('Report')   #获取名为Report的sheet
    #在第11行添加标题栏
    head = ['蔬菜','批发市场','日期','大宗价','最高价','最低价','交易量','产地']
    for j in range(8):
        sheetNew.row(10).write(j,head[j])
    #填补蔬菜栏的空白
    tempVeg =''
    for j in range(11, nrows):
        if sheetOrigin.cell_value(j,0) is not "":
            #print(j)
            tempVeg = sheetOrigin.cell_value(j, 0)
            j += 1
        else:
            sheetNew.write(j, 0, tempVeg)
            j += 1

    #填补批发市场的空白
    tempMarket =''
    for j in range(11, nrows):
        if sheetOrigin.cell_value(j, 1) is not "":
            #print(j)
            tempMarket = sheetOrigin.cell_value(j, 1)
            j += 1
        else:
            sheetNew.write(j, 1, tempMarket)
            j += 1
    print(i,'已完成填补批发市场')
    #修改日期单元格
    for j in range(13, nrows):
        datevalue = sheetOrigin.cell_value(j, 2)
        sheetNew.write(j, 2, datevalue[9:])
        j += 1
    #保存
    workbookNewPath = newdir + r'\\' + newdirs[i]
    workbookNew.save(workbookNewPath)
    i += 1
