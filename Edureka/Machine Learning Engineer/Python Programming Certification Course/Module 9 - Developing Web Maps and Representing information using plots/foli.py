import folium

map=folium.Map(location=[38.2,-99.1],zoom_start=6,tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[12.958016, 77.744033],popup="Hello",icon=folium.Icon(color="green")))
map.add_child(fg)

map.save("folium.html")
print(map)


import folium

map=folium.Map(location=[38.2,-99.1],zoom_start=6,tiles="Mapbox Bright")

fg=folium.FeatureGroup(name="Volcanoes")

for coordinate in([38.2,-99.1],[33.58,-98.09]):
    fg.add_child(folium.Marker(location=coordinate,popup="Hi, I am a Marker",icon=folium.Icon(color="green")))

map.add_child(fg)

map.save("folium.html")
print(map)

