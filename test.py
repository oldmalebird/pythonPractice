#每行显示每个蔬菜重点县主产的蔬菜名称
import pandas as pd

#读取原始数据
docAddress = r"D:\Data\蔬菜主产区\各县预计要统计的蔬菜种类--20190428.xlsx"
df_origin = pd.read_excel(
    docAddress,
    sheet_name='Sheet1',
)
print(df_origin.head(5))

counties = df_origin["区域"]

#新建一个dataframe，存放读取的dataframe
df = pd.DataFrame(columns=["区域", "省/直辖市", "主产蔬菜品种"])
'''
print(df.head(5))

print('新df的行数：', len(df.index))
print(type(df['产品'][0]) == str)
print(df['产品'][0].startswith('月'))

#如果‘产品’列在i行有月份信息，则’截至时间'列的i行数据为该月份信息
for i in range(0, len(df.index)):
    if type(df['产品'][i]) == str:
        if df['产品'][i].startswith('月'):
            df['截至时间'][i] = df['产品'][i]
    i += 1

#填补产品列的空白
tempStr = ''
for i in range(0, len(df.index)):
    if type(df['产品'][i]) == str:
        tempStr = df['产品'][i]
        i += 1
    else:
        df['产品'][i] = tempStr
        i += 1

#填补截至时间列的空白
tempMonth = ''
for i in range(0, len(df.index)):
    if type(df['截至时间'][i]) == str:
        tempMonth = df['截至时间'][i]
        i += 1
    else:
        df['截至时间'][i] = tempMonth
        i += 1

#填补时间列并删除时间列的空格
df['时间'] = df['截至时间'].str.slice(10)
df['时间'] = df['时间'].str.replace('年', '-')
df['时间'] = df['时间'].str.replace(' ', '')
df['时间'] = df['时间'].str.replace('月', '-1')
#转成时间格式
df['时间'] = pd.to_datetime(df['时间']).dt.date

#删除无意义行
df.dropna(subset=['贸易方式'], inplace=True)
print('删除无意义行后的行数：', len(df.index))

#专门处理大蒜和蘑菇数据：标准化名称
df['产品'] = df['产品'].str.replace('大蒜（加工保藏）', '大蒜（加工）')
df['产品'] = df['产品'].str.replace('大蒜（鲜冷冻）', '大蒜')
df['产品'] = df['产品'].str.replace('蘑菇  （干）', '蘑菇（干）')
#专门处理大蒜和蘑菇数据：删除蘑菇干以外的蘑菇数据
# df = df.loc[df['产品'] != '蘑菇（加工）']
# df = df.loc[df['产品'] != '蘑菇（鲜冷冻）']

#填补类别信息
vegCatAddress = r"D:\Data\信息中心进出口\数据处理\vlookup.xlsx"
vegCat = pd.read_excel(vegCatAddress, sheet_name='产品分类')
print(vegCat.head())
print(vegCat.tail())
df_merge = pd.merge(df, vegCat, how='left')

#将类别移到第二列
cols = list(df_merge)
cols.insert(1, cols.pop(cols.index('类别')))
df_merge = df_merge.ix[:, cols]
print('填补类别信息后的行数', len(df_merge.index))

#删除“蔬菜种子.”
df_merge = df_merge.loc[df_merge['产品'] != '蔬菜种子.']
print('删除‘蔬菜种子.’的行数：', len(df_merge.index))

#删除重复项
df_merge.drop_duplicates(keep='first', inplace=True)
print('删除重复项后的行数：', len(df_merge.index))

#添加不含合计的数据
df_no_sum = df_merge.loc[df_merge['贸易方式'] != '贸易方式合计']
print('不含合计数的行数：', len(df_no_sum.index))

#写入excel文件
writer = pd.ExcelWriter(r"D:\Desktop\蔬菜水果_贸201811.xlsx")
df_no_sum.to_excel(writer, sheet_name='Cleaned', index=False)
df_merge.to_excel(writer, sheet_name='Cleaned含贸易方式合计', index=False)
writer.save()
writer.close()
#python D:\Github\customs_vegetable_data\提取贸易方式进出口数据.py
'''
