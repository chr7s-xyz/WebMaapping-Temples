import folium
import pandas

    # dir(folium)
    # help(folium.Map)

data=pandas.read_csv("NewAncientTemples.csv")
data[['latitude','longitude']]=data["Coordinates"].str.split(',',expand=True)



latitude=list(data["latitude"])
longitude=list(data["longitude"])
data_place=list(data["templeName"])
description=list(data["Description"])

map=folium.Map(location=(20,77),zoom_start=5)




xyz=folium.FeatureGroup(name="MyMap")

for lat,long,place,description in zip(latitude,longitude,data_place,description):
    html=f""" <p>{place}<br>
Description :{description}</p>"""
    # print(lat.lstrip("(")+" "+long.rstrip(")"))
    iframe=folium.IFrame(html=html,width=800,height=200)
    # xyz.add_child(folium.Marker(location=[float(lat.lstrip("(")),float(long.rstrip(")"))],popup=place,icon=folium.Icon(color="green")))
    xyz.add_child(folium.Marker(location=[float(lat.lstrip("(")),float(long.rstrip(")"))],popup=folium.Popup(iframe),icon=folium.Icon(color="green")))
    
  
map.add_child(xyz)
map.save("India.html")
    
