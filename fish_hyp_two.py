import pandas as pd
import random

# define Fish class and its property
class Fish():
    def __init__(self, sub_reg):
        self.l_dic = l_dic
        self.common = ''
        self.length = 0
        self.get_common(sub_reg)
        self.get_common_lngth()

    def get_common(self, sub_reg):
        random_num = random.random()
        for common in sub_reg:
            min_val, max_val = sub_reg[common]
            if max_val > random_num >= min_val:
                self.common = common

    def get_common_lngth(self):
        self.length = self.l_dic[self.common][random.randint(0, len(self.l_dic[self.common]) - 1)] + random.random() * (
            -1 if random.random() > 0.5 else 1)


# define Angler and its property
class Anglers():
    def __init__(self, tol_common_num, size_limit):
        self.tol_common_num = tol_common_num
        self.caught_common = []
        self.caught_fish = []  # each fish with its common/length
        self.size_limit = size_limit
        self.complete = False
        self.fishing_num = 0

    def fishing(self, sub_reg, sub_reg_num):
        for i in range(sub_reg_num):
            fish = Fish(sub_reg)
            self.fishing_num += 1
            if self.check_fish(fish):
                if fish.common not in self.caught_common:
                    self.caught_common.append(fish.common)
                    if len(self.caught_common) >= self.tol_common_num:
                        self.complete = True
                        break

    def check_fish(self, fish):
        if fish.common in not_allowed or not self.check_lngth_limit(fish):
            return False
        return True

    def check_lngth_limit(self, fish):
        common_limit = self.size_limit.get(fish.common, None)
        lngth = fish.length * 0.3937
        if common_limit:
            min_size = common_limit['min_size']
            if min_size and lngth <= min_size:
                return False
            max_size = common_limit['max_size']
            if max_size and lngth >= max_size:
                return False
        return True

    def get_complete(self):
        return self.complete

# define fish class
def fish_distribution(reg_code):
    df = df1[df1['SUB_REG'] == reg_code]
    df = df[df['common'].isin(normal_spe)]
    tol_regionfish = len(df)
    df = df.groupby(['common']).agg({'common': 'count'})

    #     df.columns = ['count']
    fish_dis = {}
    split_num = 0
    for i in range(len(df)):
        new_num = split_num + df.iloc[i]['common'] / tol_regionfish
        fish_dis[df.index[i]] = [split_num, new_num]
        split_num = new_num
    return fish_dis


def simulate_onereg(sub_reg, times):
    angler = Anglers(100, size_limit)
    angler.fishing(sub_reg, times)
    return angler.caught_common


def simulate_commons(times_in_reg, tol_times, need_common_num):
    min_fishing = tol_times + 1
    goods_p = []
    for i in times_in_reg:
        for j in times_in_reg:
            if j[1] + i[1] >= tol_times:
                continue
            for _ in range(10):
                times_a = random.randint(i[0], i[-1])
                times_b = random.randint(j[0], j[-1])
                times_c = tol_times - times_a - times_b

                angler = Anglers(need_common_num, size_limit)
                angler.fishing(north_atlantic, times_a)
                angler.fishing(mid_atlantic, times_b)
                angler.fishing(south_atlantic, times_c)
                if angler.get_complete() and angler.fishing_num < min_fishing:
                    min_fishing = angler.fishing_num
                    goods_p = [times_a, times_b, angler.fishing_num - times_a - times_b]
    return min_fishing, goods_p

# FILTER CONDITION -- REGULATION
not_allowed = ['RED DRUM']
size_limit = {'RED SNAPPER': {'min_size': 16, 'max_size': None},
              'GRAY SNAPPER': {'min_size': 12, 'max_size': None},
              'SHEEPSHEAD': {'min_size': 12, 'max_size': None},
              'striped bass': {'min_size': 28, 'max_size': None},
              'HADDOCK': {'min_size': 18, 'max_size': None},
              'SCUP': {'min_size': 9, 'max_size': None},
              'STRIPED BASS': {'min_size': 14, 'max_size': None},
              'ATLANTIC CROAKER': {'min_size': 9, 'max_size': None},
              'DOLPHIN': {'min_size': 20, 'max_size': None},
              'PINFISH': {'min_size': 2, 'max_size': None},
              'BLACK SEA BASS': {'min_size': 12.5, 'max_size': None},
              'KING MACKEREL': {'min_size': 24, 'max_size': None},
              'SPANISH MACKEREL': {'min_size': 12, 'max_size': None},
              'VERMILION SNAPPER': {'min_size': 10, 'max_size': None},
              'YELLOWTAIL SNAPPER': {'min_size': 12, 'max_size': None},
              'RED PORGY': {'min_size': 14, 'max_size': None},
              'LANE SNAPPER': {'min_size': 8, 'max_size': None},
              'GRAY TRIGGERFISH': {'min_size': 12, 'max_size': None},
              'SAND SEATROUT': {'min_size': 15, 'max_size': None},
              'BLUE RUNNER': {'max_size': 20, 'min_size': None},
              'SOUTHERN FLOUNDER': {'min_size': 14, 'max_size': None}
              }

# read raw data and choose
df = pd.concat(map(pd.read_csv, ['size_20211.csv', 'size_20212.csv', 'size_20213.csv',
                                 'size_20214.csv', 'size_20215.csv', 'size_20216.csv']))

size_df = pd.concat(map(pd.read_csv, ['size_20211.csv', 'size_20212.csv', 'size_20213.csv',
                                      'size_20214.csv', 'size_20215.csv', 'size_20216.csv']))
size_df = size_df[['YEAR', 'common', 'WGT', 'LNGTH', 'SUB_REG']]
df1 = size_df.loc[size_df['common'].notna() & size_df['LNGTH'].notna()]

# The species' prob under 0.5% are removed from fishing list
tol_fishing = len(df1) * 0.005
l_dic = {}
species = set(df1['common'])

for key in species:
    l_normal_spe = list(df1[df1['common'] == key]['LNGTH'])
    if len(l_normal_spe) < tol_fishing:
        continue
    l_dic[key] = l_normal_spe

normal_spe = list(l_dic.keys())


north_atlantic = fish_distribution(4)
mid_atlantic = fish_distribution(5)
south_atlantic = fish_distribution(6)
gulf_mexico = fish_distribution(7)

# a, b, c, d which represents the simulation in north atlantic,  mid atlantic, south atlantic and gulf mexico
# respectively
a = simulate_onereg(north_atlantic, 500)
b = simulate_onereg(mid_atlantic, 500)
c = simulate_onereg(south_atlantic, 500)
d = simulate_onereg(gulf_mexico, 500)

print(len(a))
print(len(b))
print(len(c))
print(len(d))

# conclusion 1: south_atlantic has the most species


times_in_reg = [(i * 50, (i + 1) * 50) for i in range(30)]
tol_times = 1500
print(simulate_commons(times_in_reg, tol_times, 35))

# conclusion 2: if angler want to catch fish common over than 35, it should have fish trip at least no more than 200.