


from tabulate import tabulate

import requests #we access the website from this module




def prayer_data():
    year = '2020' #current year for url
    timezone = 'America/Chicago' #must be in America/Chicago format
    lat = '38.0043264' #lat in decimal format
    lon = '-87.3627648' #lon in decimal format
    method = '0' #calculation method for prayer
    both = 'false' #if you want to see both asr prayer times depending on method selected
    time = '1' #controls if am or pm or 24 hour clock format shown
    dateStart = ' '
    dateEnd = 'May 24'

    url = 'https://www.moonsighting.com/time_json.php?year=' + year + '&tz=' + timezone +'&lat=' + lat + '&lon=' + lon + '&method=' + method + '&both=' + both + '&time=' + time
    #above line is parsed url with user data
    response = requests.get(url) #sending request with url and formdata change from post

    if response.status_code == 200: #we reached the website success!
        prayertimes = response.json() #convert to json

        #todo figure out a way to depoloy it on a website setting.
        #this prints the headers of the table
        print("Date/Day    \tFajr     Sunrise     Dhur         Asr         Maghrib       Isha")
        print("----------------------------------------------------------------------------------")
        printvalues = True #if the user entered a date then this becomes false
        if dateStart == " ":
            printvalues = True
        else:
            printvalues = False
        for x in prayertimes['times']: #loops through time data from the api
           if printvalues: 
                print(x['day'], "| ", x['times']['fajr'], "| ", x['times']['sunrise'], "| ", x['times']['dhuhr'], "| ",
                      x['times']['asr'], "| ", x['times']['maghrib'], "| ", x['times']['isha'],
                      "|")  # prints the date Jan 01 Wed
                print("----------------------------------------------------------------------------------")
           if len(dateStart) > 1 and dateStart in x['day']:
               print(x['day'], "| " ,x['times']['fajr'], "| ", x['times']['sunrise'], "| ",x['times']['dhuhr'], "| ", x['times']['asr'], "| ", x['times']['maghrib'], "| ",x['times']['isha'], "|") #prints the date Jan 01 Wed
               print("----------------------------------------------------------------------------------")
               printvalues = True
           if len(dateEnd) > 1 and dateEnd in x['day']:
               print("date end: ", dateEnd)
               print("x day: ", x['day'])
               print(len(dateEnd))
               print("break")
               break

          #print(x, '->', prayertimes[x])
          #dates  = prayertimes['times'][0]['day']

        #print(fajr)
    else:
        print("failed") #did not get data



prayer_data()
