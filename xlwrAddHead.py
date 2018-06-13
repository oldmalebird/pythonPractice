#添加标题栏，xlwt只能保存为excel2003文件

import xlrd
import xlwt
from xlutils.copy import copy



print(1)
workbook = xlrd.open_workbook(r"D:\p\p001\test.xlsx")

sheet1 = workbook.sheet_by_index(0)
print(sheet1.name, sheet1.nrows, sheet1.ncols)
nrows = sheet1.nrows
ncols = sheet1.ncols

print(sheet1.cell(0,0))

book = copy(workbook)
sheet2 = book.get_sheet('Sheet1')
sheet2.write(0,0,10000)
head = ['蔬菜','批发市场','日期','大宗价','最高价','最低价','交易量','产地']

for i in range(0,8):
    sheet2.row(10).write(i,head[i])
    print('正在修改第'+str(i)+'个标题栏')

book.save(r"D:\p\p001\test2.xls")
