



import requests #we access the website from this module
import json



def prayer_data():
    latitude = 38.0043264 #test case form data
    longitude = -87.3627648 #test case form data
    timeformat = "24 hours" #test case form data
    #url = 'https://www.moonsighting.com/pray.php' #url where data is stored
    url = 'https://www.moonsighting.com/time_json.php?year=2020&tz=America/Chicago&lat=38.0043264&lon=-87.3627648&method=0&both=false&time=0'
    form_data = {          #parameters to fill in table
    'Latitude:': 38.0043264,
    'longitude:': -87.3627648,
    'time': 1,
    'Make Timetable': 'Make Timetable',
    } #not needed url takes care of passing parameters

    response = requests.get(url, data =form_data) #sending request with url and formdata change from post

    if response.status_code == 200: #we reached the website success!
        prayertimes = response.json() #convert to json

       # print(response.text) #print what we got this will be trimmed
        print(prayertimes)  #todo parse prayer times
    else:
        print("failed") #did not get data




prayer_data()