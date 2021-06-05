
import pandas

# Using Pandas
data=pandas.read_csv("Volcanoes_USA.txt")
print(data)
print(type(data))

lon=list(data["LON"])
print(lon)

lat=list(data["LAT"])
print(lat)

elev=list(data["ELEV"])
print(elev)



