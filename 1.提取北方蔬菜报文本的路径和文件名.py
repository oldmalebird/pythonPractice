# -*- coding:utf-8*-
#读取filelist.txt，如果该行结尾为.txt，则把该路径存储到dirList里面，把文件名存储到titleList里面
import os
import re
import chardet
#建立北方蔬菜报文件地址空列表
dirList = []
#建立北方蔬菜报txt文件地址空列表
dirTxtList = []
#建立北方蔬菜报文件名空列表
titleFileList = []
#建立北方蔬菜报标题空列表
titleList = []

with open(r"D:\Data\小程序\北方蔬菜报\filelist.txt") as dirfile:
    for line in dirfile:
        #print(line)
        line = line.strip()
        #print(line)
        #print(type(line))
        dirList.append(line)
        if line.endswith('.txt'):
            # print(line)
            dirTxtList.append(line)
            title = line.split('\\')
            # print('1', title)
            # print('2', line)
            title = title[-1]
            # print(title)
            titleFileList.append(title)
            title = title[:-4]
            titleList.append(title)
            print(title)

# print(dirTxtList)
# 按行打印所有txt文件的路径
# for i in range(len(dirTxtList)):
print('finish part 1.')
