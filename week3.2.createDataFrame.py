'''已知有一个列表中存放了一组音乐数据：

music_data = [("the rolling stones","Satisfaction"),("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),("Metallica","Nothing Else Matters")]

请根据这组数据创建一个如下的DataFrame：

               singer             song_name
1  the rolling stones          Satisfaction
2             Beatles             Let It Be
3       Guns N' Roses             Don't Cry
4           Metallica  Nothing Else Matters
'''
# -*- coding: utf-8 -*-
"""
create DataFrame object

@author: Dazhuang
"""
import pandas as pd
music_data = [("the rolling stones","Satisfaction"),("Beatles","Let It Be"),("Guns N' Roses","Don't Cry"),("Metallica","Nothing Else Matters")]
music_table = pd.DataFrame(music_data)
music_table.index = range(1, 5)
music_table.columns = ['singer', 'song_name']
print(music_table)
