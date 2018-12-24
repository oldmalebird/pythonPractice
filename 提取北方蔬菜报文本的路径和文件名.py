#读取filelist.txt，如果该行结尾为.txt，则把该路径存储到dirList里面，把文件名存储到titleList里面

import re

dirList = []
titleList = []
with open(r"D:\Data\小程序\北方蔬菜报\filelist.txt") as dirfile:
    for line in dirfile:
        #print(line)
        line = line.strip()
        #print(line)
        #print(type(line))
        dirList.append(line)
        if line.endswith('.txt'):
            print(line)
            dirList.append(line)
            #title = line.find('(D:\Data\小程序\北方蔬菜报\\).txt')

print(dirList)
