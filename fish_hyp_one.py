import pandas as pd
import pandas as pd
import numpy as np
from datetime import datetime
import random
from datetime import date, timedelta
import doctest

df = pd.concat(map(pd.read_csv, ['size_20211.csv', 'size_20212.csv', 'size_20213.csv',
                                 'size_20214.csv', 'size_20215.csv', 'size_20216.csv']))
# Concatenate multiple csv files into one dataframe.
df1 = df.loc[df['LNGTH'].notna()]  # Keep rows with valid length value
df1 = df1[['YEAR', 'common', 'LNGTH', 'WGT', 'ID_CODE']]  # Kept columns are year, common name, length, weight, and date
df1['ID_CODE'] = pd.to_datetime(df1['ID_CODE'].astype(str).str[5:-3],
                                format='%Y%m%d')  # change date dat into proper datetime format
winter_days = datetime(2021, 1, 1), datetime(2021, 3, 31)
summer_days = datetime(2021, 7, 1), datetime(2021, 9, 30)


def get_dict_fish(date):
    """Given a date range, return a dictionary of fish species and numbers of each caught that day. :param date:
    datetime format of start date and end date. >>> test_date = datetime(2021,1, 1),datetime(2021,1, 10) >>> list(
    get_dict_fish(test_date).items())[0] ('2021-01-01', {'SAND SEATROUT': 11, 'SHEEPSHEAD': 10, 'SOUTHERN KINGFISH':
    6, 'WHITE GRUNT': 5, 'HARDHEAD CATFISH': 4, 'GRAY SNAPPER': 4, 'WHITE CATFISH': 2, 'ATLANTIC CROAKER': 1,
    'RED DRUM': 1, 'BLACK DRUM': 1})
    """
    daterange = pd.date_range(date[0], date[-1])
    dict_name = {}
    for i in daterange:
        mask = df1.loc[df1['ID_CODE'] == i]['common'].value_counts()[0:20]
        mask = dict(mask)
        day = {str(i)[0:10]: {}}
        day[str(i)[0:10]].update(mask)
        dict_name.update(day)
        dict_fish_day = dict_name
    return dict_fish_day


dict_winter = get_dict_fish(winter_days)
dict_summer = get_dict_fish(summer_days)


def get_fish_stat(date):
    """Given a date range, return a dictionary of fish species and their length and weight values.
    :param date: datetime format of start date and end date.
    >>> test_date = datetime(2021,1, 1),datetime(2021,1, 10)
    >>> list(get_fish_stat(test_date).items())[0]
    ('ALMACO JACK', {'max_lngth': 437.0, 'min_lngth': 300.0, 'mean_lngth': 368.5, 'max_wgt': 1.4, 'min_wgt': 0.46, 'mean_wgt': 0.9299999999999999})
    """
    fish_stat = {}
    mask = (df1['ID_CODE'] > date[0]) & (df1['ID_CODE'] < date[-1])
    loc_data = df1.loc[mask]
    fish_range = loc_data.groupby('common').agg({'LNGTH': ['max', 'min', 'mean'], 'WGT': ['max', 'min', 'mean']})
    fish_range.columns = ['max_lngth', 'min_lngth', 'mean_lngth', 'max_wgt', 'min_wgt', 'mean_wgt']
    for i in range(len(fish_range)):
        temp_dict = {fish_range.index[i]: dict(fish_range.iloc[i])}
        fish_stat.update(temp_dict)
    return fish_stat


dict_stat_winter = get_fish_stat(winter_days)
dict_stat_summer = get_fish_stat(summer_days)


def get_fish_chance(date):
    """Given a date range, return a dictionary of fish species and their probability distribution in percentage.
    :param date: datetime format of start date and end date.
    >>> test_date = datetime(2021,1, 1),datetime(2021,1, 10)
    >>> list(get_fish_chance(test_date).items())[0]
    ('BLACK MARGATE', 0.173)
    """
    dict_chance = {}
    mask = (df1['ID_CODE'] > date[0]) & (df1['ID_CODE'] < date[-1])
    loc_data = df1.loc[mask]
    for species in loc_data['common'].unique():
        fish_count = loc_data.loc[loc_data['common'] == species]['common'].count()
        chance = fish_count / len(loc_data)
        temp_dict1 = {species: round(chance * 100, 3)}
        dict_chance.update(temp_dict1)
    return dict_chance


fish_chance_winter = get_fish_chance(winter_days)
fish_chance_summer = get_fish_chance(summer_days)


def compute(fish_chance, dict_stat, prob_threshold=0.01):
    # Probability threshold finds fish species with its distribution greater than 0.01%
    fish_species = list(filter(lambda x: x[1] > 0.01, fish_chance.items()))

    species_keyset = set(dict(fish_species).keys())
    feature_keyset = set(dict_stat.keys())
    fish_key = species_keyset.intersection(feature_keyset)

    species_result = dict(filter(lambda x: x[0] in fish_key, fish_species))
    feature_result = dict(filter(lambda x: x[0] in fish_key, dict_stat.items()))
    species_result_sort = sorted(species_result.items(), key=lambda x: x[1], reverse=False)

    species_prob = {}
    fish_sum = 0
    total = sum(species_result.values())
    for s in species_result_sort:
        species_prob[s[0]] = [fish_sum / total, (fish_sum + s[1]) / total]
        fish_sum += s[1]

    return species_prob, feature_result


def get_species(prob, species_prob):
    for (k, v) in species_prob.items():
        if v[0] <= prob < v[1]:
            return k
    else:
        return None


def generate_info(prob, feature_result, species_prob):
    species = get_species(prob, species_prob)
    feature = feature_result[species]
    length = random.uniform(feature['min_lngth'], feature['max_lngth'])
    weight = random.uniform(feature['min_wgt'], feature['max_wgt'])
    return species, length, weight


def fishing(fish_chance, dict_stat):
    """Generate a fish, with its size and weight data.
    :param fish_chance:the probability distribution of each species of fish
    :param dict_stat: the length and weight data of fish
    >>> test_date = datetime(2021,1, 1),datetime(2021,1, 10)
    >>> test_fish_stat = get_fish_stat(test_date)
    >>> test_fish_chance = get_fish_chance(test_date)
    >>> len(fishing(test_fish_chance,test_fish_stat))
    3
    """
    species_prob, feature_result = compute(fish_chance, dict_stat)
    prob = random.random()
    return generate_info(prob, feature_result, species_prob)


def main(random_seed):
    """Simulate fishing, compare mean length of all fish caught betwene summer and winter.
    :param random_seed: a random seed
    >>> main(2019)
    'Winter is the winner.'

    """
    people_season = ['winter', 'summer']
    fishing_time = 1000
    random.seed(random_seed)
    result = []
    for p, s in enumerate(people_season):
        # print('*'*10,'PERSON',p , 'in',s,'*'*10)
        for t in range(fishing_time):
            info = [p, s]
            if s == 'winter':
                info.extend(fishing(fish_chance_winter, dict_stat_winter))
            else:
                info.extend(fishing(fish_chance_summer, dict_stat_summer))
                # print(info)
            result.append(info)

    outdf = pd.DataFrame(result, columns=['person', 'season', 'species', 'length', 'weight'])
    result = outdf.groupby(['season'])[['length', 'weight']].apply(np.mean)
    lengthRes = result['length']['summer'] > result['length']['winter']
    weightRes = result['weight']['summer'] > result['weight']['winter']
    length_winter = result['length']['winter']
    length_summer = result['length']['summer']


    if lengthRes and weightRes:
        winner = 'Summer is the winner.'
    elif not lengthRes and not weightRes:
        winner = 'Winter is the winner.'
    else:
        winner = 'They ended in a draw.'

    outdf.to_csv('record.txt', mode='a', sep='\t', index=True, header=True)
    f = open('record.txt', mode='a')
    f.writelines(f'Average length for fish caught in winter is {round(length_winter,2)}mm \n')
    f.writelines(f'Average length for fish caught in summer is {round(length_summer,2)}mm \n')
    f.writelines([winner, '\n\n'])
    f.close()
    return winner


if __name__ == "__main__":
    doctest.testmod(verbose=True)
