#!/usr/bin/python3
""" Geolocation via IP Lookup """


from urllib import request
import json

try:
    data = json.load(request.urlopen('http://ipinfo.io/json'))
    latlong = data['loc'].split(',')
    lat = latlong[0]
    long = latlong[1]

    print(data)
except Exception as e:
    print(e)
else:
    print('You are near: {city}, {region}, {postal}, {country}'.format(**data))
    print('Lat: {}'.format(lat))
    print('Lng: {}'.format(long))




