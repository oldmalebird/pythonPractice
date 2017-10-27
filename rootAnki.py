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
rootObverse = []
rootReverse = []
rootTag = []
rootTable = {'Obverse': rootObverse, 'Reverse':rootReverse, 'tag': rootTag}
#frame = DataFrame(rootTable)

count = 0
rootData = open('root.txt')
for line in rootData:
    line = line.rstrip()
    if re.search('^[0-9]',line):
        count += 1
        rootObverse.append(line)
        rootTag.append('root')
#print(count)
#count = 22
#print(rootObverse)

#f.open('root.txt','r')
with open('root.txt') as f:
    rootFileLines = f.readlines()
    print('len(rootFileLines)',len(rootFileLines))
    #存储词根所在的行号的列表
    lineNumber = []
    for i in range(0, len(rootFileLines)):
        if re.search('^[0-9]', rootFileLines[i]):
            lineNumber.append(i)
    #print(lineNumber)
    #[0, 25, 56, 79, ......, 4231]
    #继续编程，试试还能不能从rootFileLines读取东西
    #print(rootFileLines[4])  可以继续读取
    for i in range(0, len(lineNumber)-1):
        temp = ''
        #oneReverseLines = lineNumber[i+1]-lineNumber[i]
        for j in range(lineNumber[i]+1,lineNumber[i+1]): # if i = 0: j in (1,25)
            if j < lineNumber[i+1]-1:
                temp += rootFileLines[j]+'\n'
            else:
                temp += rootFileLines[j]
        rootReverse.append(temp)
    temp2 = ''
    print("lineNumber[-1]+1:", lineNumber[-1]+1)
    for k in range(lineNumber[-1]+1, len(rootFileLines)):
        if k< len(rootFileLines)-1:
            temp2 += rootFileLines[k]+'\n'
        else:
            temp2 += rootFileLines[k]
    rootReverse.append(temp2)

rootTable = {'Obverse': rootObverse, 'Reverse':rootReverse, 'tag': rootTag}
#frame = DataFrame(rootTable)
frame = DataFrame(rootTable)
frame.to_csv("testRoot.csv",index=False)
