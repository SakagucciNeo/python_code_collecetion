import folium
import pandas as pd


# # このCSVには、県庁所在地の緯度・経度がlatitudeカラムとlongitudeカラムに入っている。
# df_prefecture = pd.read_csv("../data/prefectural_capital_locations.csv")

df = pd.read_excel(
    'C:/Users/user/Documents/GitHub/python_code_collecetion/onsen_output01.xlsx')


def visualize_locations(df,  zoom=15, tiles="Stamen Terrain"):
    """日本を拡大した地図に、pandasデータフレームのlatitudeおよびlongitudeカラムをプロットする。
    """

    # 図の大きさを指定する。
    f = folium.Figure(width=1000, height=500)

    # 初期表示の中心の座標を指定して地図を作成する。
    center_lat = df["緯度"][1]
    center_lon = df["経度"][1]
    m = folium.Map([center_lat, center_lon], zoom_start=zoom).add_to(f)

    # データフレームの全ての行のマーカーを作成する。
    for i in range(0, len(df)):
        folium.Marker(location=[df["緯度"][i],
                      df["経度"][i]]).add_to(m)

    return m


visualize_locations(df)
