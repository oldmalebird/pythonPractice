import chardet
import os
'''
# 把所有txt文件都合并到all.txt文件中
all = open(r"D:\Data\小程序\北方蔬菜报\2017\all.txt", 'a+', encoding='UTF-8')
print('finish part 2.')
for i in range(len(dirTxtList)):
    # 增加rb后无UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 16
    f = open(dirTxtList[i], 'rb')
    #变成str才可以用encode，然后还要把byte还原为str，才可以与\n相连
    all.write(str(str(f.read()).encode('utf-8')) + '\n')
    #all.write(f.read())
    #f.read()
    print('finish read')
'''
# 把所有txt文件都合并到all.txt文件中
all = open(r"D:\Data\小程序\北方蔬菜报\2017\all.txt", 'w', encoding='UTF-8')
print('finish open all.txt')
for line in open(r"D:\Data\小程序\北方蔬菜报\txt文件地址2.txt"):
    # 增加rb后无UnicodeDecodeError: 'gbk' codec can't decode byte 0xa4 in position 16
    address = line.strip()
    f = open(address)
    # print(address)
    # print(chardet.detect(f.read())['encoding'])
    #变成str才可以用encode，然后还要把byte还原为str，才可以与\n相连
    # all.write(str(str(f.read()).encode('utf-8')) + '\n')
    # all.write(str(str(f.read().decode(chardet.detect(str(f.read()))['encoding'])).encode('utf-8')) + '\n')
    # all.write(f.read())
    # print(str(f.read().decode(str(chardet.detect(f.read())['encoding']))))
    # all.write(str(f.read())) 用这行可写入到1.20
    # all.write(str(str(f.read()).encode('utf-8')) + '\n') 用这行可写入到1.20
    try:
        all.write(str(f.read()))
        # print('finish read')
    except:
        print(address)

all.close()
