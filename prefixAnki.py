# -*- coding: utf-8 -*-
'''伪代码:
两个字符串数组a,b
如果以数字为开头,该行为一个字符串
下一行至下一个以数字为开头那一行之前的一行为一个字符串
两个字符串分别放在excel的两列'''

#cd desktop/python/pythonPractice

import re
import pandas as pd #需要用里面的data frame
from pandas import DataFrame

#储存正面、背面、标签的list
prefixObverse = []
prefixReverse = []
prefixTag = []
prefixTable = {'Obverse': prefixObverse, 'Reverse':prefixReverse, 'tag': prefixTag}
#frame = DataFrame(prefixTable)

count = 0
prefixData = open('prefix.txt')
for line in prefixData:
    line = line.rstrip()
    if re.search('-$',line) or re.search('^[a-z]+-[^a-zA-Z]', line):
        count += 1
        prefixObverse.append(line)
        prefixTag.append('prefix')
print('count:',count)
#count = 114
#print(prefixObverse)

with open('prefix.txt') as f:
    prefixFileLines = f.readlines()
    #prefixFileLines.decode('unicode-escape')
    print('len(prefixFileLines)',len(prefixFileLines))
    #存储后缀所在的行号的列表
    lineNumber = []
    for i in range(0, len(prefixFileLines)):
        if re.search('-$', prefixFileLines[i]) or re.search('^[a-z]+-[^a-zA-Z]', prefixFileLines[i]):
            lineNumber.append(i)
    #print(lineNumber)
    #[0, 25, 56, 79, ......, 4231]
    #继续编程，试试还能不能从prefixFileLines读取东西
    #print(prefixFileLines[4])  可以继续读取
    for i in range(0, len(lineNumber)-1):
        temp = ''
        for j in range(lineNumber[i]+1,lineNumber[i+1]): # if i = 0: j in (1,25)
            if j < lineNumber[i+1]-1:
                prefixFileLines[j] = prefixFileLines[j].rstrip()
                temp += prefixFileLines[j]+'\n'
            else:
                temp += prefixFileLines[j]
        prefixReverse.append(temp)
    temp2 = ''
    print("lineNumber[-1]+1:", lineNumber[-1]+1)
    for k in range(lineNumber[-1]+1, len(prefixFileLines)):
        if k < len(prefixFileLines)-1:
            prefixFileLines[k] = prefixFileLines[k].rstrip()
            temp2 += prefixFileLines[k]+'\n'
        else:
            temp2 += prefixFileLines[k]
    prefixReverse.append(temp2)

prefixTable = {'Obverse': prefixObverse, 'Reverse':prefixReverse, 'tag': prefixTag}
#frame = DataFrame(prefixTable)
frame = DataFrame(prefixTable)
frame.to_csv("testprefix.csv", index = False, encoding = 'utf-8')
#print(type(frame.iloc[5,1]))
