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
suffixObverse = []
suffixReverse = []
suffixTag = []
suffixTable = {'Obverse': suffixObverse, 'Reverse':suffixReverse, 'tag': suffixTag}
#frame = DataFrame(suffixTable)

count = 0
suffixData = open('suffix.txt')
for line in suffixData:
    line = line.rstrip()
    if re.search('^-',line):
        count += 1
        suffixObverse.append(line)
        suffixTag.append('suffix')
print('count:',count)
#count = 166
#print(suffixObverse)

with open('suffix.txt') as f:
    suffixFileLines = f.readlines()
    #suffixFileLines.decode('unicode-escape')
    print('len(suffixFileLines)',len(suffixFileLines))
    #存储后缀所在的行号的列表
    lineNumber = []
    for i in range(0, len(suffixFileLines)):
        if re.search('^-', suffixFileLines[i]):
            lineNumber.append(i)
    #print(lineNumber)
    #[0, 25, 56, 79, ......, 4231]
    #继续编程，试试还能不能从suffixFileLines读取东西
    #print(suffixFileLines[4])  可以继续读取
    for i in range(0, len(lineNumber)-1):
        temp = ''
        for j in range(lineNumber[i]+1,lineNumber[i+1]): # if i = 0: j in (1,25)
            if j < lineNumber[i+1]-1:
                suffixFileLines[j] = suffixFileLines[j].rstrip()
                temp += suffixFileLines[j]+'\n'
            else:
                temp += suffixFileLines[j]
        suffixReverse.append(temp)
    temp2 = ''
    print("lineNumber[-1]+1:", lineNumber[-1]+1)
    for k in range(lineNumber[-1]+1, len(suffixFileLines)):
        if k < len(suffixFileLines)-1:
            suffixFileLines[k] = suffixFileLines[k].rstrip()
            temp2 += suffixFileLines[k]+'\n'
        else:
            temp2 += suffixFileLines[k]
    suffixReverse.append(temp2)

suffixTable = {'Obverse': suffixObverse, 'Reverse':suffixReverse, 'tag': suffixTag}
#frame = DataFrame(suffixTable)
frame = DataFrame(suffixTable)
frame.to_csv("testsuffix.csv", index = False, encoding = 'utf-8')
#print(type(frame.iloc[5,1]))
