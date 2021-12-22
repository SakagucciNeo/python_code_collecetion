import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
import pandas as pd

df = pd.read_excel(
    'C:/Users/user/Documents/GitHub/python_code_collecetion/sentou.xlsx')

df['緯度'] = float(0)
df['経度'] = float(0)

small_df = df.iloc[0:4]
print(small_df)


def get_lat_lon_from_address(address_l):
    """
    address_lにlistの形で住所を入れてあげると、latlonsという入れ子上のリストで緯度経度のリストを返す関数。
    >>>>get_lat_lon_from_address(['東京都文京区本郷7-3-1','東京都文京区湯島３丁目３０−１'])
    [['35.712056', '139.762775'], ['35.707771', '139.768205']]
    """
    url = 'http://www.geocoding.jp/api/'
    latlons = []
    for address in tqdm(address_l):
        payload = {"v": 1.1, 'q': address}
        r = requests.get(url, params=payload)
        ret = BeautifulSoup(r.content, 'lxml')
        if ret.find('error'):
            raise ValueError(f"Invalid address submitted. {address}")
        else:
            lat = ret.find('lat').string
            lon = ret.find('lng').string
            latlons.append([lat, lon])
            time.sleep(10)
    return latlons


for index, row in small_df.iterrows():

    print(row)
    print(row.住所)
    lotlons = get_lat_lon_from_address(["'" + row.住所 + "'"])

    print(lotlons[0][0])
    print(type(lotlons[0][0]))

    print(lotlons[0][1])
    print(type(lotlons[0][1]))

    print(small_df.at[index, '緯度'])
    print(small_df.at[index, '経度'])

    small_df.at[index, '緯度'] = float(lotlons[0][0])
    small_df.at[index, '経度'] = float(lotlons[0][1])

print(small_df)

sort_df = small_df.sort_values(by='経度')
print(sort_df)

sort_df.to_excel('onsen_output01.xlsx', sheet_name='sheet_name')
