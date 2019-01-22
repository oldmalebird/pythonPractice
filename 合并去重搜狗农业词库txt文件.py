# -*-coding:utf-8-*-
import os

in_path = r"D:\Data\小程序\北方蔬菜报\worddict"
fin_path = [fname for fname in os.listdir(in_path) if fname[-4:] == ".txt"]
print(fin_path)
veg_words = []
for f in fin_path:
    print("f: ", f)
    lines = open(os.path.join(in_path, f), 'r', encoding='utf-8')
    #lines = open(os.path.join(in_path, f))
    for line in lines:
        veg_words.append(line.strip())
    print('现在收录的农业用词有：', len(veg_words))
    lines.close()

veg_words = set(veg_words)
print('去重后的农业用词有：', len(veg_words))  #3.7w

# 写入veg_dict.txt自定义词库
veg_dict = open(r"D:\Data\小程序\北方蔬菜报\veg_dict.txt",
                'w')  # 这个需要保存成utf-8才可以被jieba读取
veg_dict.write('\n'.join(veg_words))
veg_dict.close()
