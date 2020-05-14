import pandas as pd
import os
docAddress = r"D:\Data\2019价格监测系统\历史数据\季度累计播种面积\2018季度累计播种面积"
areaDocList = os.listdir(docAddress)
print(areaDocList)
#创建空dataframe
df = pd.DataFrame(columns=[
    "品种", "本季度蔬菜累计播种面积", "上年同期数", "比上年同期增减%", "本季度露地蔬菜累计播种面积", "上年同期数1",
    "比上年同期增减%1", "本季度小棚蔬菜累计播种面积", "上年同期数2", "比上年同期增减%2", "本季度大中棚蔬菜累计播种面积",
    "上年同期数3", "比上年同期增减%3", "本季度温室蔬菜累计播种面积", "上年同期数4", "比上年同期增减%4", "备注", "年",
    "季度", "省/直辖市"
])

#遍历、合并所有文件
for i in range(len(areaDocList)):
    docName = areaDocList[i]
    docAddress = r"D:\Data\2019价格监测系统\历史数据\季度累计播种面积\2018季度累计播种面积"
    docAddress += '\\' + docName
    print("本次打开的文件名为：", docName)
    print("本次打开的文件路径为：", docAddress)
    df_temp = pd.read_excel(
        docAddress,
        #sheet_name='（三）主要蔬菜面积季度调查表',
        header=None,
        names=[
            "品种", "本季度蔬菜累计播种面积", "上年同期数", "比上年同期增减%", "本季度露地蔬菜累计播种面积",
            "上年同期数1", "比上年同期增减%1", "本季度小棚蔬菜累计播种面积", "上年同期数2", "比上年同期增减%2",
            "本季度大中棚蔬菜累计播种面积", "上年同期数3", "比上年同期增减%3", "本季度温室蔬菜累计播种面积", "上年同期数4",
            "比上年同期增减%4", "备注"
        ],
        skiprows=20,
        skipfooter=7)

    df_temp["年"] = docName.split(".")[0].split('-')[0]
    df_temp["季度"] = docName.split(".")[0].split('-')[1]
    df_temp["省/直辖市"] = docName.split(".")[0].split('-')[2]
    df = df.append(df_temp)
    print("第" + str(i) + "个文件append成功")
    df['省/直辖市'] = df['省/直辖市'].str.replace('区', '')
    df['省/直辖市'] = df['省/直辖市'].str.replace('省', '')

writer = r"D:\Data\2019价格监测系统\历史数据\季度累计播种面积\2018季度累计播种面积.xlsx"
df.to_excel(writer, sheet_name="季度累计播种面积", index=False)
