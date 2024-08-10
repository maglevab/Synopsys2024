import pandas as pd
import geopy
import requests
geolocator = geopy.Nominatim(user_agent='pythonProject')

def get_state(lat, lon):
    url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&namedetails=1&accept-language=en&zoom=3'
    try:
        result = requests.get(url=url)
        result_json = result.json()
        print(result_json)
        return result_json['address']['country_code'].upper()
    except:
        return None
def get_zipcode(latitude, longitude):
    location = geolocator.reverse((latitude, longitude))
    print(location)
    return location.raw['address']['postcode']

print(get_zipcode(37.27408490021866, -122.02609574983406))

fakePoles = pd.read_csv("/Users/arahan/Downloads/fakeData4SQLv2.csv")
scaledZipcodeData = pd.read_csv("/Users/arahan/Downloads/scaledZipcodeData.csv")
scaledZipcodeDataList = scaledZipcodeData.values.tolist()

def get_zipcode(latitude, longitude):
    location = geolocator.reverse((latitude, longitude))
    return location.raw['address']['postcode']



for i in range(len(fakePoles["POLE_LAT"])):
    latitude = fakePoles['POLE_LAT'][i]
    longitude = fakePoles['POLE_LONG'][i]

    try:
        index = scaledZipcodeDataList.index(get_zipcode(latitude, longitude))
    except ConnectionError:
        print("NOT ABLE TO CONNECT")
    print(scaledZipcodeData.iloc[index])
