'''伪代码:
两个字符串数组a,b
如果以数字为开头,该行为一个字符串
下一行至下一个以数字为开头那一行之前的一行为一个字符串
两个字符串分别放在excel的两列'''

#cd desktop\

import re
'''
import pandas as pd #需要用里面的data frame


#储存正面、背面、标签的list
rootObverse = []
rootReverse = []
rootTag = []

#f.open('root.txt','r')
with open('root.txt') as f:
    rootFileLines = f.readlines()
    for i in range(0, len(rootFileLines)):
        if

        '''
#不管用help(rstrip)
help(str.rstrip)
count = 0
hand = open('root.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^[0-9]',line):
        count += 1
        #print(line)
print(count)
