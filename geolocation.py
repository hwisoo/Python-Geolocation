#!/usr/bin/python3
""" Geolocation via IP Lookup """


from urllib import request
import json
import folium

try:
    data = json.load(request.urlopen('http://ipinfo.io/json'))


    print(data)
except Exception as e:
    print(e)
else:
    latlong = data['loc'].split(',')
    lat = float(latlong[0])
    long = float(latlong[1])
    print('You are near: {city}, {region}, {postal}, {country}'.format(**data))

    print('Lat: {}'.format(lat))
    print('Lng: {}'.format(long))


map = folium.Map(location=[lat, long], zoom_start=6, tiles='Stamen Terrain')
map.save('location.html')

