



import requests #we access the website from this module




def prayer_data():
    latitude = 38.0043264 #test case form data
    longitude = -87.3627648 #test case form data
    timeformat = "24 hours" #test case form data
    url = 'https://www.moonsighting.com/pray.php' #url where data is stored

    form_data = {          #parameters to fill in table
    'Latitude:': latitude,
    'longitude:': longitude,
    'time': '1',
    'Make Timetable': 'Make Timetable',
    }

    response = requests.post(url, form_data) #sending request with url and formdata

    if response.status_code == 200: #we reached the website success!
        print(response.text) #print what we got this will be trimmed

    else:
        print("failed") #did not get data




prayer_data()