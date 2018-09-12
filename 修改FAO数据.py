import pandas as pd
doclist = [
    '2000-2016全球农畜产品出口量（蔬菜）.xlsx', '2000-2016全球农畜产品出口额（蔬菜）.xlsx',
    '2000-2016全球农畜产品进口量（蔬菜）.xlsx', '2000-2016全球农畜产品进口额（蔬菜）.xlsx',
    '2000-2016全球生产者价格（蔬菜）.xlsx', '2000-2016农业生产量价值（蔬菜）.xlsx',
    '2000-2016农作物产量（蔬菜）.xlsx', '2000-2016农作物面积（蔬菜）.xlsx'
]
doclist_forsql = [
    'areaHarvested.xlsx', 'exportQuantity.xlsx', 'exportValue.xlsx',
    'grossProductionValue.xlsx', 'importQuantity.xlsx', 'importValue.xlsx',
    'producerPrice.xlsx', 'production.xlsx'
]

for i in range(len(doclist)):
    docName = doclist[i]
    doc_address = r'D:\Data\from zzh\全球蔬菜\可视化\只含蔬菜'
    doc_address += '\\' + docName
    print('Index:', i, "本次打开的文件名为：", docName)
    df = pd.read_excel(doc_address)
    print(len(df))
    #删除醋栗、加仑
    df = df[(True ^ df["item - Chinese"].isin(['醋栗', '加仑']))]
    print(len(df))
    #替换"Beans, green"，“Beans, dry”和 "String beans"的翻译
    df.loc[df.Item == 'Beans, green', 'item - Chinese'] = '豇豆'
    df.loc[df.Item == 'Beans, dry', 'item - Chinese'] = '脱水豇豆'
    df.loc[df.Item == 'String beans', 'item - Chinese'] = '菜豆'
    save_address = r'D:\Data\from zzh\全球蔬菜\可视化\只含蔬菜不含醋栗'
    save_address += '\\' + docName
    writer = save_address
    df.to_excel(writer, sheet_name=docName[:-5], index=False)
    print('已导出')

for i in range(len(doclist_forsql)):
    docName = doclist_forsql[i]
    doc_address = r'D:\Data\from zzh\全球蔬菜\可视化\只含蔬菜\forSQL'
    doc_address += '\\' + docName
    print('Index:', i, "本次打开的文件名为：", docName)
    df = pd.read_excel(doc_address)
    print(len(df))
    #删除醋栗、加仑
    df = df[(True ^ df["item_Chinese"].isin(['醋栗', '加仑']))]
    print(len(df))
    #替换"Beans, green"，“Beans, dry”和 "String beans"的翻译
    df.loc[df.Item == 'Beans, green', 'item_Chinese'] = '豇豆'
    df.loc[df.Item == 'Beans, dry', 'item_Chinese'] = '脱水豇豆'
    df.loc[df.Item == 'String beans', 'item_Chinese'] = '菜豆'
    save_address = r'D:\Data\from zzh\全球蔬菜\可视化\只含蔬菜不含醋栗\forSQL'
    save_address += '\\' + docName
    writer = save_address
    df.to_excel(writer, sheet_name=docName[:-5], index=False)
    print('已导出')
