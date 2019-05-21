#!/usr/bin/python3
""" Geolocation via IP Lookup """


from urllib import request
import json

try:
    data = json.load(request.urlopen('http://ipinfo.io/json'))
    print(data)
except Exception as e:
    print(e)
else:
    print('You are near: {city}, {region}, {postal}, {country}'.format(**data))
    print('        Lat/Lng: {}E'.format(data['loc'].replace(',', 'N, ')))
