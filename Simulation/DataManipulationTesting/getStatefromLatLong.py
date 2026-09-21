import requests
import mysql.connector
from time import sleep

def get_state_from_latlng(lat, lng, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        for result in data['results']:
            for component in result['address_components']:
                if 'administrative_area_level_1' in component['types']:
                    return component['short_name']
    return None
    # Replace with your actual latitude, longitude, and API key


mydb = mysql.connector.connect(
  host="localhost",
  port="8889",
  user="root",
  password="root",
  database='Substation'
)

mycursor = mydb.cursor()
query = 'SELECT * FROM substationv4latlong;'
mycursor.execute(query)

results = []
for row in mycursor.fetchall():
    results.append(row)



lat = 0
long = 0
api_key = 'AIzaSyDfTU-yjmZGAXiRzU4KMtGoEQ12rtJJTeQ'
counter = 0
for i in range(len(results)):
    if len(results[i][3]) >= 1:
        print(results[i])
        continue
    lat = results[i][0]
    long = results[i][1]
    print(lat, long)
    state = get_state_from_latlng(lat, long, api_key)
    query = "UPDATE substationv4latlong SET SUB_STATE = '" + state + "' WHERE SUB_LAT = " + str(lat) + ' AND SUB_LONG = ' + str(long) + ';'
    print(query)
    print(counter)
    mycursor.execute(query)
    counter += 1
    if counter == 50:
        counter = 0
        sleep(7)
    mydb.commit();





