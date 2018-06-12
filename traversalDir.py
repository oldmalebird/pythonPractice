# -*- coding: utf-8 -*
'''
遍历文件夹中的文件
'''

import os
dir = "D:\p\p001"
dirs = os.listdir(dir)
for dirc in dirs:
    print(dirc)
print(type(dirs))
print(dirs)
