from geopy.distance import geodesic

# (緯度, 経度)
HachimanYu = (35.647952, 139.666309)
KomanoYu = (35.642944, 139.667165)

dis1 = geodesic(HachimanYu, KomanoYu).m

print(dis1)