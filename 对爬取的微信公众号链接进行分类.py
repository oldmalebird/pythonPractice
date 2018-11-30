import pandas as pd

#导入文件，只提取date,title,link三列
df = pd.read_csv("zhongguoshucai.csv")
df = df[['date', 'title', 'link']]

#去除某些date字段末尾的“原创”二字
df['date'].replace('原创$', '', regex=True, inplace=True)
#去除title字段以“原创”开头且接两处换行符和若干空格的部分替换成“【原创】”
df['title'].replace('^原创\n\s+\n\s+', '【原创】', regex=True, inplace=True)
#按date字段降序排列，但是顺序为：9,8,7,6,5,4,3,2,1,11,10
df.sort_values(by=['date'], ascending=False, inplace=True)

#提取title中含番茄的信息
tomato = df.copy()
tomato["bool"] = tomato.title.str.contains("番茄|西红柿|茄果|瓜果")
tomato = tomato[tomato["bool"] == True]
tomato = tomato[['date', 'title', 'link']]
#提取title中含椒的信息
pepper = df.copy()
pepper["bool"] = pepper.title.str.contains("椒")
pepper = pepper[pepper["bool"] == True]
pepper = pepper[['date', 'title', 'link']]
#提取title中含黄瓜的信息
cucumber = df.copy()
cucumber["bool"] = cucumber.title.str.contains("黄瓜")
cucumber = cucumber[cucumber["bool"] == True]
cucumber = cucumber[['date', 'title', 'link']]
#提取title中含茄但不是番茄的信息
eggplant = df.copy()
eggplant["bool"] = eggplant.title.str.contains("茄")
eggplant = eggplant[eggplant["bool"] == True]
eggplant['bool2'] = ~eggplant.title.str.contains('番茄')
eggplant = eggplant[eggplant["bool2"] == True]
eggplant = eggplant[['date', 'title', 'link']]
eggplant = eggplant[['date', 'title', 'link']]
#提取title中含西甜瓜的信息
melon = df.copy()
melon["bool"] = melon.title.str.contains("西瓜|甜瓜|西甜瓜|瓜果")
melon = melon[melon["bool"] == True]
melon = melon[['date', 'title', 'link']]
#提取title中含草莓的信息
strawberry = df.copy()
strawberry["bool"] = strawberry.title.str.contains("草莓")
strawberry = strawberry[strawberry["bool"] == True]
strawberry = strawberry[['date', 'title', 'link']]

#保存至同一个excel
writer = pd.ExcelWriter("D:\Github\蔬菜微信公众号\分类_中国蔬菜.xlsx")
tomato.to_excel(excel_writer=writer, sheet_name="番茄", index=False)
pepper.to_excel(excel_writer=writer, sheet_name="辣椒", index=False)
cucumber.to_excel(excel_writer=writer, sheet_name="黄瓜", index=False)
eggplant.to_excel(excel_writer=writer, sheet_name="茄子", index=False)
melon.to_excel(excel_writer=writer, sheet_name="西甜瓜", index=False)
strawberry.to_excel(excel_writer=writer, sheet_name="草莓", index=False)
writer.save()
writer.close()
