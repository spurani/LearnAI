# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:17:47 2020

@author: SP
"""
import pandas as pd
import folium
table = pd.read_csv("775_m9_datasets_v1.0/Police_Department_Incidents_Year_2016_.csv")
table = table.head(100)
lon = table["X"]
lat = table["Y"]
map = folium.Map(location=[lat.mean(),lon.mean()],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Crime Scene")

for lt,ln in zip(lat,lon):
    fgv.add_child(folium.Marker(location=(lt,ln),popup="Crime Scene",icon=folium.Icon(color="green")))
map.add_child(fgv)
map.save("BasicWebMap.html")

table_2 = table.loc[table['Category'] == "ROBBERY"]
table_2 = table_2.head(7)
lon = table_2["X"]
lat = table_2["Y"]
map = folium.Map(location=[lat.mean(),lon.mean()],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Crime Scene")

for lt,ln in zip(lat,lon):
    fgv.add_child(folium.Marker(location=(lt,ln),popup="Crime Scene",icon=folium.Icon(color="green")))
map.add_child(fgv)
map.save("BasicWebMap_1.html")

table_3 = table.loc[(table['Category'] == "GAMBLING") | (table['Category'] == "FRAUD") ]
table_3 = table.head(15)
lon = table_3["X"]
lat = table_3["Y"]
map = folium.Map(location=[lat.mean(),lon.mean()],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Crime Scene")

for lt,ln in zip(lat,lon):
    fgv.add_child(folium.Marker(location=(lt,ln),popup="Crime Scene",icon=folium.Icon(color="green")))
map.add_child(fgv)
map.save("BasicWebMap_2.html")

table_4 = table.loc[table['Category'] == "BULGARY"]
table_4 = table.head(7)
lon = table_4["X"]
lat = table_4["Y"]
map = folium.Map(location=[lat.mean(),lon.mean()],zoom_start=6,tiles="Mapbox Bright")
fgv=folium.FeatureGroup(name="Crime Scene")

for lt,ln in zip(lat,lon):
    fgv.add_child(folium.Marker(location=(lt,ln),popup="Crime Scene",icon=folium.Icon(color="green")))
map.add_child(fgv)
map.save("BasicWebMap_3.html")