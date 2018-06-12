import xlrd
import xlwt


print(1)
workbook = xlrd.open_workbook(r"D:\p\p001\test.xlsx")

sheet1 = workbook.sheet_by_index(0)
print(sheet1.name, sheet1.nrows, sheet1.ncols)
nrows = sheet1.nrows
ncols = sheet1.ncols
