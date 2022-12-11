import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import random
from datetime import date, timedelta
import copy
import matplotlib.pyplot as plt
from collections import Counter

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

d1 = df[['common', 'LNGTH', 'WGT']].dropna()
k = df1.groupby('common').agg({'LNGTH': ['max', 'min', 'mean'], 'WGT': ['max', 'min', 'mean']})
k.columns = ['max_lngth', 'min_lngth', 'mean_lngth', 'max_wgt', 'min_wgt', 'mean_wgt']
for i in range(len(k)):
    temp_dict = {k.index[i]: dict(k.iloc[i])}
    fish_stat.update(temp_dict)

dict_chance = {}
for species in df1['common'].unique():
    zz = df1.loc[df1['common'] == species]['common'].count()
    temp_dict1 = {species: round((zz / len(df1) * 100), 3)}
    dict_chance.update(temp_dict1)

#Set the probability
prob_threshold=0.01 #%
fish_species=list(filter(lambda x:x[1]>0.01,dict_chance.items()))
species_keyset=set(dict(fish_species).keys())
feature_keyset=set(fish_stat.keys())
fish_key=species_keyset.intersection(feature_keyset)
species_result=dict(filter(lambda x:x[0] in fish_key,fish_species))
feature_result=dict(filter(lambda x:x[0] in fish_key,fish_stat.items()))

#Set different bait probabilities
def with_bait(bait):
    species_result_sort=sorted(bait.items(),key=lambda x:x[1], reverse=False)
    species_prob=dict()
    accSum=0
    total=sum(bait.values())
    for s in species_result_sort:
        species_prob[s[0]]=[accSum/total,(accSum+s[1])/total]
        accSum+=s[1]
    return species_prob

#Set the range at which the fish will take the bait
def getSpecies(bait, prob):
    for (k, v) in bait.items():
        if prob >= v[0] and prob < v[1]:
            return k
    else:
        return None

def generateInfor(bait, prob):
    species = getSpecies(bait, prob)
    feature = feature_result[species]
    length = random.uniform(feature['min_lngth'], feature['max_lngth'])
    weight = random.uniform(feature['min_wgt'], feature['max_wgt'])
    return species, length, weight

#Look for changes in fish abundance
#Catch 100 fish at a time. Catch 100 times
def mean_sepcies(number_round,fishing_count,bait):
    total = []
    for p in range(number_round):
        un_species=[]
        for t in range(fishing_count):
            prob=random.random()
            info=generateInfor(bait,prob)[0]
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
    plt.close(fig)
    t = df.total_species.value_counts()
    mean = df.total_species.values.mean()
    return mean

# The average species per 100 cycles, 20 cycles
def mean_change(total_round, number_round, fishing_times, bait):
    res = []
    for i in range(total_round):
        a = mean_sepcies(number_round, fishing_times, bait)
        res.append([i, a])

    df2 = pd.DataFrame(res, columns=['count', 'mean_sepcies'])
    fig, ax = plt.subplots()
    x = df2['count']
    y = df2['mean_sepcies']
    ax.plot(x, y, color='orange')
    plt.title('species with by round')
    plt.xlabel('times')
    plt.ylabel('number')
    plt.ylim(20, 60)
    return df2

#Look for structural changes in the fish
def number(bait):
    fish=[]
    for t in range(100):
        prob=random.random()
        info=generateInfor(bait,prob)
        fish.append(info[0])
    counter = Counter(fish)
    return counter

#generate dataframe
def structure(shrimp_number,Mackerel_number,nolure_number):
    same = set(shrimp_number).intersection(set(Mackerel_number)).intersection(set(nolure_number))
    df_training = pd.DataFrame(np.nan, index=list(same), columns=['nolure','shrimp','Mackerel'])
    for i in same:
        df_training.at[i,'nolure'] = int(nolure_number[i])
        df_training.at[i,'shrimp'] = int(shrimp_number[i])
        df_training.at[i,'Mackerel'] = int(Mackerel_number[i])
    df_training['nolure'] = df_training['nolure'].astype(int)
    df_training['shrimp'] = df_training['shrimp'].astype(int)
    df_training['Mackerel'] = df_training['Mackerel'].astype(int)
    return df_training

'''Total 139 fish species, probability less than 0.06 is an interval (number 47, mean probability 0.026), 
probability between 0.06 and 0.35 is an interval (number 46, mean probability 0.168), 
probability greater than 0.35 is an interval (number 46, mean probability 1.97)'''

#Two types of baits were formulated, mackerel as the superior bait,
# shrimp as the normal bait and nolure as the no-bait control
Mackerel = copy.deepcopy(species_result)
shrimp = copy.deepcopy(species_result)
no_lure = copy.deepcopy(species_result)

#Increase the probability of rare fish depending on the bait
for i,k in species_result.items():
    if k<0.06:
        Mackerel[i]=k+1.95
        shrimp[i] = k+0.14

#Different fish bait catch probabilities
with_Mackerel = with_bait(Mackerel)
with_shrimp = with_bait(shrimp)
no_lure = with_bait(no_lure)

#Start the simulation
mean_sepcies(50,100,with_Mackerel)
mean_sepcies(50,100,with_shrimp)
mean_sepcies(50,100,no_lure)

#Look at the average of different kinds every 50 times, and loop 20 times
df_shirmp = mean_change(20,50,100,with_shrimp)
df_nolure = mean_change(20,50,100,no_lure)
df_Mackerel=mean_change(20,50,100,with_Mackerel)

#fish abundant graph
fig, ax = plt.subplots()
x = df_shirmp['count']
y = df_shirmp['mean_sepcies']
x1 = df_nolure['count']
y1 = df_nolure['mean_sepcies']
x2 = df_Mackerel['count']
y2 = df_Mackerel['mean_sepcies']
ax.plot(x,y,label='shirmp')
ax.plot(x1,y1,label='no lure')
ax.plot(x2,y2,label='Mackerel')
plt.title('species by round')
plt.xlabel('times')
plt.ylabel('number')
# plt.ylim(20,80)
plt.legend()
plt.show()

#Changes in fish number structure
shrimp_number = number(with_shrimp)
Mackerel_number = number(with_Mackerel)
nolure_number = number(no_lure)

print(structure(shrimp_number,Mackerel_number,nolure_number))