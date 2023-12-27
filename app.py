# importing modules/packages/etc
import folium
import pandas

    # dir(folium)
    # help(folium.Map)


# dataframes for required data
data_temple=pandas.read_csv("NewAncientTemples.csv")
data_aqi=pandas.read_csv("aqi.csv")



#getting list for all series required in Map
data_temple[['latitude','longitude']]=data_temple["Coordinates"].str.split(',',expand=True)
latitude_temple=list(data_temple["latitude"])
longitude_temple=list(data_temple["longitude"])
data_temple_place=list(data_temple["templeName"])
description=list(data_temple["Description"])

latitude_aqi=list(data_aqi["lat"])
longitude_aqi=list(data_aqi["lng"])
rating_aqi=list(data_aqi["AQI Category"])
city=list(data_aqi["City"])
aqi_value=list(data_aqi["AQI Value"])


# function to set color of circle marker according to aqi rating
def RateAqi(rating):
    if(rating == "Good"):
        color = 'green'
    elif(rating== "Moderate"):
        color="orange"
    else:
        color="red"
    return color
        

# map creation
map=folium.Map(location=(20,77),zoom_start=5)

#children to be added in the map
aqiObject=folium.FeatureGroup(name="Air Quality Index")
templeObject=folium.FeatureGroup(name="Temples")


#looping through temples data 
for lat,long,place,description in zip(latitude_temple,longitude_temple,data_temple_place,description):
    html=f""" <p>{place}<br>
    Description :{description}</p>"""
    # print(lat.lstrip("(")+" "+long.rstrip(")"))
    iframe=folium.IFrame(html=html,width=800,height=200)
    # templeObject.add_child(folium.Marker(location=[float(lat.lstrip("(")),float(long.rstrip(")"))],popup=place,icon=folium.Icon(color="green")))
    templeObject.add_child(folium.Marker(location=[float(lat.lstrip("(")),float(long.rstrip(")"))],popup=folium.Popup(iframe),icon=folium.Icon(color="green")))


# looping through airQualityIndex data
for lat,long,aqi_rating,city,aqi_value in zip(latitude_aqi,longitude_aqi,rating_aqi,city,aqi_value):
    html=f""" <p>AQI Value :{str(aqi_value)} </p> """
    # print(lat.lstrip("(")+" "+long.rstrip(")"))
    iframe=folium.IFrame(html=html,width=400,height=100)
    color_circle=RateAqi(aqi_rating)
    aqiObject.add_child(folium.CircleMarker([lat,long],radius=8,fill=True,color=color_circle,fill_color=color_circle,popup=folium.Popup(iframe),tooltip=city,opacity=1))
    
 
# adding childs with layer control and saving map
map.add_child(aqiObject)
map.add_child(templeObject)
map.add_child(folium.LayerControl())
map.save("index.html")
    
