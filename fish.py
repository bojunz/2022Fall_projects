import padas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import random
from datetime import date, timedelta
import random

df = pd.concat(map(pd.read_csv, ['size_20211.csv', 'size_20212.csv', 'size_20213.csv',
                                 'size_20214.csv', 'size_20215.csv', 'size_20216.csv']))

df1 = df.loc[df['LNGTH'].notna()]  # 数据集去掉没有数据的行
df1 = df1[['YEAR', 'common', 'LNGTH', 'WGT', 'ID_CODE']]  # 保留的列，[年，鱼的名字，长度，重量，日期代码]
df1['ID_CODE'] = pd.to_datetime(df1['ID_CODE'].astype(str).str[5:-3], format='%Y%m%d')  # 把日期做成datetime格式
len(df1)

start_date = date(2021, 1, 1)
end_date = date(2021, 12, 31)
daterange = pd.date_range(start_date, end_date)  # 设置起始和结束日期

a = {}  # 创建一个大字典，key是日期，值是当天钓到鱼的数量
for i in daterange:
    s = df1.loc[df1['ID_CODE'] == i]['common'].value_counts()[0:20]
    s = dict(s)
    b = {str(i)[0:10]: {}}
    b[str(i)[0:10]].update(s)
    a.update(b)
dict_fish_day = a

list_fish = list(df['common'].dropna().unique())
fish_stat = {}  # 这个字典key是鱼的名字，值是鱼的最大长度，最小长度，平均长度，最大重量，最小重量，平均重量

d1 = df[['common', 'LNGTH', 'WGT']].dropna()
k = df1.groupby('common').agg({'LNGTH': ['max', 'min', 'mean'], 'WGT': ['max', 'min', 'mean']})
k.columns = ['max_lngth', 'min_lngth', 'mean_lngth', 'max_wgt', 'min_wgt', 'mean_wgt']
# for i in ff['common']:
for i in range(len(k)):
    temp_dict = {k.index[i]: dict(k.iloc[i])}
    fish_stat.update(temp_dict)


dict_chance = {}  # 这个字典是每种鱼出现的概率（一年中）
for species in df1['common'].unique():
    zz = df1.loc[df1['common'] == species]['common'].count()
    temp_dict1 = {species: round((zz / len(df1) * 100), 3)}
    dict_chance.update(temp_dict1)


prob_threshold = 0.01  # %
fish_species = list(filter(lambda x: x[1] > 0.01, dict_chance.items()))

species_keyset = set(dict(fish_species).keys())
feature_keyset = set(fish_stat.keys())
fish_key = species_keyset.intersection(feature_keyset)
len(fish_key)

species_result = dict(filter(lambda x: x[0] in fish_key, fish_species))
feature_result = dict(filter(lambda x: x[0] in fish_key, fish_stat.items()))
species_result_sort = sorted(species_result.items(), key=lambda x: x[1], reverse=False)

species_prob = dict()
accSum = 0
total = sum(species_result.values())
for s in species_result_sort:
    species_prob[s[0]] = [accSum / total, (accSum + s[1]) / total]
    accSum += s[1]


def getspecies(prob):
    for (k, v) in species_prob.items():
        if prob >= v[0] and prob < v[1]:
            return k
    else:
        return None


def generateinfo(prob):
    species = getspecies(prob)
    feature = feature_result[species]
    length = random.uniform(feature['min_lngth'], feature['max_lngth'])
    weight = random.uniform(feature['min_wgt'], feature['max_wgt'])
    return species, length, weight



people_count = 5
fishing_time = 3



result = []
for p in range(people_count):
    print('*' * 10, 'PERSON ', p, '*' * 10)
    for t in range(fishing_time):
        prob = random.random()
        info = generateinfo(prob)
        print(info)
        result.append((p, info))
print(result)
