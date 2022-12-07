import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import random
from datetime import date, timedelta

# import os
# os.chdir('/Users/mission/Downloads/ps_2021_csv')
# os.getcwd()

df = pd.concat(map(pd.read_csv, ['size_20211.csv', 'size_20212.csv','size_20213.csv',
                                 'size_20214.csv','size_20215.csv','size_20216.csv']))

df1 = df.loc[df['LNGTH'].notna()]
df1 = df1[['YEAR','common','LNGTH','WGT','ID_CODE']]
df1['ID_CODE'] = pd.to_datetime(df1['ID_CODE'].astype(str).str[5:-3], format='%Y%m%d')

start_date = date(2021,1, 1)
end_date = date(2021, 12, 31)
daterange = pd.date_range(start_date, end_date)

a = {}
for i in daterange:
    s  = df1.loc[df1['ID_CODE']== i]['common'].value_counts()[0:20]
    s = dict(s)
    b = {str(i)[0:10]:{}}
    b[str(i)[0:10]].update(s)
    a.update(b)
dict_fish_day = a

list_fish = list(df['common'].dropna().unique())
fish_stat = {}


d1 = df[['common','LNGTH','WGT']].dropna()
k = df1.groupby('common').agg({'LNGTH':['max','min','mean'],'WGT':['max','min','mean']})
k.columns = ['max_lngth','min_lngth','mean_lngth','max_wgt','min_wgt','mean_wgt']
for i in range(len(k)):
    temp_dict = {k.index[i]:dict(k.iloc[i])}
    fish_stat.update(temp_dict)

dict_chance = {}
for species in df1['common'].unique():
    zz = df1.loc[df1['common']== species]['common'].count()
    temp_dict1 = {species:round((zz/len(df1)*100),3)}
    dict_chance.update(temp_dict1)

prob_threshold=0.01 #%
fish_species=list(filter(lambda x:x[1]>0.01,dict_chance.items()))
species_keyset=set(dict(fish_species).keys())
feature_keyset=set(fish_stat.keys())
fish_key=species_keyset.intersection(feature_keyset)
species_result=dict(filter(lambda x:x[0] in fish_key,fish_species))
feature_result=dict(filter(lambda x:x[0] in fish_key,fish_stat.items()))
species_result_sort=sorted(species_result.items(),key=lambda x:x[1], reverse=False)

species_prob=dict()
accSum=0
total=sum(species_result.values())
for s in species_result_sort:
    species_prob[s[0]]=[accSum/total,(accSum+s[1])/total]
    accSum+=s[1]


def getSpecies(prob):
    for (k, v) in species_prob.items():
        if prob >= v[0] and prob < v[1]:
            return k
    else:
        return None


def generateInfor(prob):
    species = getSpecies(prob)
    feature = feature_result[species]
    length = random.uniform(feature['min_lngth'], feature['max_lngth'])
    weight = random.uniform(feature['min_wgt'], feature['max_wgt'])
    return species, length, weight

import matplotlib.pyplot as plt

def mean_sepcies(number_round,fishing_count):
    total = []
    for p in range(number_round):
        un_species=[]
        for t in range(fishing_count):
            prob=random.random()
            info=generateInfor(prob)[0]
            un_species.append(info)
        uni = set(un_species)
        total.append([p,len(uni)])
    df =pd.DataFrame(total,columns=['count','total_species'])
    fig, ax = plt.subplots()
    x = df['count']
    y = df['total_species']
    ax.plot(x,y)
    plt.title('species by round')
    plt.xlabel('times')
    plt.ylabel('number')
    plt.show()
    t = df.total_species.value_counts()
    mean = df.total_species.values.mean()
    print('species','-','count')
    print(t[:5])
    return mean

mean_sepcies(100,100)


def mean_change(total_round, number_round, fishing_times):
    res = []
    for i in range(total_round):
        a = mean_sepcies(number_round, fishing_times)
        res.append([i, a])

    df2 = pd.DataFrame(res, columns=['count', 'mean_sepcies'])
    fig, ax = plt.subplots()
    x = df2['count']
    y = df2['mean_sepcies']
    ax.plot(x, y, color='orange')
    plt.title('species by round')
    plt.xlabel('times')
    plt.ylabel('number')
    plt.ylim(20, 60)
    plt.show()
    return True

mean_change(20,50,100)

#species count
from collections import Counter

fish=[]
for p in range(10):
    for t in range(10):
        prob=random.random()
        info=generateInfor(prob)
        fish.append(info[0])

counter = Counter(fish)
print(counter)
counter.most_common(5)