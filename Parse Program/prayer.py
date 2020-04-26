



import requests #we access the website from this module
import json



def prayer_data():
    latitude = 38.0043264 #test case form data
    longitude = -87.3627648 #test case form data
    timeformat = "24 hours" #test case form data
    #url = 'https://www.moonsighting.com/pray.php' #url where data is stored
    url = 'https://www.moonsighting.com/time_json.php?year=2020&tz=America/Chicago&lat=38.0043264&lon=-87.3627648&method=0&both=false&time=1'
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
        #print(prayertimes)  #todo make a table with this data
        #todo after making data make it so its location and methods can be changed and passed to api
        #todo figure out a way to depoloy it on a website setting. 
        #fajr = prayertimes['times'][0]  #gets first day list of prayers
        #fajr = prayertimes['times'][0]['day'] #gets the date with the day
        fajr = prayertimes['times'][0]['times']['fajr'] #this gets fajr prayer time
        #timesfajir = [] #array of times for fajir
        #timessunrise = []  # array of times for sunrise
        dates = [] #array of dates
        for x in prayertimes['times']:
          print(x)
          #print(x, '->', prayertimes[x])
          #dates  = prayertimes['times'][0]['day']

        #print(fajr)
    else:
        print("failed") #did not get data




prayer_data()