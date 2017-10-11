'''爬取自己的微信，首先安装itchat'''
import itchat
itchat.login()
#爬取自己好友相关信息，返回一个json文件
friends = itchat.get_friends(update = True)[0:]
#初始化计数器
male = female = other = 0
#friends[0]是自己，所以从friends[1]开始
for i in friends[1:]:
    sex = i['Sex']
    if sex == 1:
        male += 1
    elif sex == 2:
        female +=1
    else:
        other += 1
#计算朋友总数
total = len(friends[1:])
print('Male: %.2f%%'%(float(male)/total*100)+'\n'+'Female: %.2f%%'%(float(female)/total*100)+'\n'+'Other: %.2f%%'%(float(other)/total*100)+'\n')
