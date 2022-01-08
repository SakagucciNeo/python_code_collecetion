import pandas as pd
from pykakasi import kakasi
from geopy.distance import geodesic

# (緯度, 経度)
HachimanYu = (35.647952, 139.666309)
KomanoYu = (35.642944, 139.667165)

dis1 = geodesic(HachimanYu, KomanoYu).m

print(dis1)


kakasi = kakasi()

kakasi.setMode('H', 'a')
kakasi.setMode('K', 'a')
kakasi.setMode('J', 'a')

conv = kakasi.getConverter()

word = '八幡湯'

print(conv.do(word))

df = pd.read_excel(
    'C:/Users/user/Documents/GitHub/python_code_collecetion/onsen_output03.xlsx')
print(df)

print('indexの確認==>\n', df.index)

print(df['浴場名'])

df.insert(0, 'bath_name', '')

df.drop(['Unnamed'], axis=1)
print(df)

df.drop(df.columns[1], axis=1)
print(df.columns[1])


def convert_bathname(kanji_bathname):

    kakasi = kakasi()

    kakasi.setMode('H', 'a')
    kakasi.setMode('K', 'a')
    kakasi.setMode('J', 'a')

    conv = kakasi.getConverter()
    conved_bathname = conv.do(kanji_bathname)

    return conved_bathname


for index, row in df.iterrows():

    df.bath_name = convert_bathname(["'" + row.浴場名 + "'"])

print(df)
