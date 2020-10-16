import pandas as pd
import os

root_path = r"D:\huodian\#5"  #引号里是放文件的文件夹的路径
files = os.listdir(root_path)  #files存储了该文件夹里的文件的全名
n = len(files)  #n为文件的个数
print(n)
firstFilePath = root_path + "\\" + files[0]  #files这个列表里面的第一个文件的路径
df_full = pd.read_excel(
    firstFilePath,
    names=['颗粒物', 'SO2', 'NOX'],  #给需要读取的三列起的3个列名
    usecols="F,I,L",  #读取excel文件中的F,I,L三列
    skiprows=6,  #跳过的行数，如果跳过7行，则需要写6，因为在python里，0也是一行
    nrows=24)  #只读取24行

for i in range(1, n):  #依次读取第2到第n个excel文件中的相关内容
    fullFilePath = root_path + "\\" + files[i]
    df = pd.read_excel(
        fullFilePath,
        names=['颗粒物', 'SO2', 'NOX'],
        usecols="F,I,L",
        skiprows=6,
        nrows=24)
    df_full = pd.concat(
        [df_full, df], sort=False)  #把第n个excel文件中的数据拼接到df_full里面

writer = pd.ExcelWriter(
    r"D:\huodian\#5\测试.xlsx")  #保存到D:\huodian\#5\测试.xlsx这个文件
df_full.to_excel(writer, 'sheet1', index=False)
writer.save()
