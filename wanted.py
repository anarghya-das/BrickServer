import json
import urllib.request
from pyowm import OWM

def toarr():
    apiKey = "NMX2QYEuqSjNe8MBf6gE7uHoTSeu7KIB"
    results = 50  # 50,100,150
    contents = urllib.request.urlopen(
        "http://dataservice.accuweather.com/currentconditions/v1/topcities/" + str(
            results) + "?apikey=" + apiKey).read()
    arr = json.loads(contents)
    final=[]
    for i in range(len(arr)):
        if arr[i]['WeatherText'] not in final:
            final.append(arr[i]['WeatherText'])
    return json.dumps(final)

def getInfo(condition):
    apiKey = "NMX2QYEuqSjNe8MBf6gE7uHoTSeu7KIB"
    results = 50  # 50,100,150
    contents = urllib.request.urlopen(
        "http://dataservice.accuweather.com/currentconditions/v1/topcities/" + str(
            results) + "?apikey=" + apiKey).read()
    arr = json.loads(contents)
    al=[]
    for i in range(len(arr)):
        if arr[i]['WeatherText'] == condition:
            lon,lat,ofmap,each={},{},{},{}
            lon['Longitude'] = arr[i]['GeoPosition']['Longitude']
            lat['Latitude'] = arr[i]['GeoPosition']['Latitude']
            ofmap['Country'] = arr[i]['EnglishName']
            each.update(lat)
            each.update(lon)
            each.update(ofmap)
            al.append(each)
    return al

print(toarr())
print(getInfo('Mostly cloudy'))


            


    