#汇总全国价格
import pandas as pd
#python D:\Github\xfd_vegetable_price\汇总全国价格.py
'''docList = ['[2019-1-1—2019-11-23]冬瓜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]包心芥菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]南瓜信息速采(部省)汇总查询.xls', '[2019-1-1 —2019-11-23]四季豆信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]大白菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]大葱信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]大蒜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]娃娃菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]尖椒信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]扁豆 信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]油菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]甘蓝信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]生姜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]生菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]番茄信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]白菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]白萝卜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]空心菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]胡萝卜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]芥菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]花椰菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]花菜信息速采(部省)汇总查询.xls', '[2019-1-1 —2019-11-23]芹菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]苦瓜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]茄子信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]莲藕信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]莴 笋信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]菠菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]西兰花信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]西芹信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]西葫芦信息速采( 部省)汇总查询.xls', '[2019-1-1—2019-11-23]豆角信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]豇豆信息速采(部省)汇 总查询.xls', '[2019-1-1—2019-11-23]辣椒信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]青菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]韭菜信息速采(部省)汇总查询.xls', '[2019-1-1—2019-11-23]黄瓜信息速采(部省)汇总查询.xls']
'''
#提取第一个文件
'''
parse_cols : int or list, default None
Deprecated since version 0.21.0: Pass in usecols instead.
usecols : int or list, default None
If None then parse all columns,
If int then indicates last column to be parsed
If list of ints then indicates list of column numbers to be parsed
If string then indicates comma separated list of Excel column letters and column ranges (e.g. “A:E” or “A,C,E:F”). Ranges are inclusive of both sides.
'''
df = pd.read_excel(
    r"D:\中国蔬菜协会data\生产者价格\[2019-1-1—2019-11-23]丝瓜信息速采(部省)汇总查询.xls]",
    sheet_name='丝瓜信息速采(部省)',
    header=None,
    names=["蔬菜", "省", "价格", "日期"],
    skiprows=1)
#print(df.describe())
print(df.head())
#print(df.describe())
print(df.tail())
#提取其他文件
'''
for i in range(1, len(docList)):
    print('i=', i)
    docName = docList[i]
    doc_address = r'C:\Users\MaleBird\Desktop\2018_01_06'
    doc_address += '\\' + docName
    print("本次打开的文件名为：", docName)
    df_temp = pd.read_excel(
        doc_address,
        sheet_name='Report',
        header=None,
        name=["蔬菜", "省", "市", "批发市场", "日期", "大宗价", "最高价", "最低价", "交易量", "产地"],
        skiprows=11,
        skipfooter=3)
    #print(df_temp.head())
    df = df.append(df_temp)
    #print(df.tail())
    i += 1
print(df.tail())

writer = r'C:\Users\MaleBird\Desktop\201812.xlsx'
df.to_excel(writer, sheet_name='201812')
print('已导出')
#python D:\Github\xfd_vegetable_price\汇总全国价格.py'''
'''
