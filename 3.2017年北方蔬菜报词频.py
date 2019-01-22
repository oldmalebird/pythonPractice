import re  # 正则表达式库
import collections  # 词频统计库
import numpy as np  # numpy数据处理库
import jieba  # 结巴分词
# import wordcloud  # 词云展示库
# from PIL import Image  # 图像处理库
# import matplotlib.pyplot as plt  # 图像展示库

# 读取文件
fn = open(r"D:\Data\小程序\北方蔬菜报\2017\all.txt", 'r', encoding='utf-8')  # 打开文件
string_data = fn.read()  # 读出整个文件
fn.close()  # 关闭文件

# 文本预处理
pattern = re.compile(
    u'\t|\n|\.|-|:|;|\)|\(|\?|"|：|“|”|）|；|？|（|　|，|。|、')  # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data)  # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all=False)  # 精确模式分词
object_list = []
# stopwords = stopwordslist(r"D:\Github\pythonPractice\stopwords_raw.txt")

lines = open(r"D:\Github\pythonPractice\stopwords.txt", 'r', encoding='utf-8')
stopwords = []
for line in lines.readlines():
    stopwords.append(line.strip())  #将去除了回车符号的停用词增加到停用词列表
print(stopwords)

for word in seg_list_exact:  # 循环读出每个分词
    if word not in stopwords:  # 如果不在停用词列表中
        object_list.append(word)  # 分词追加到列表

# 词频统计
word_counts = collections.Counter(object_list)  # 对分词做词频统计
word_counts_top_n = word_counts.most_common(1000)  # 获取前1000最高频的词
for word, count in word_counts_top_n:
    print(word, count)  # 输出检查
