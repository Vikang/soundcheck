import json
import random
import requests

def get_songs():
    numOfPages = str(1)

    #response = requests.get("http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key=db917afb597e2be5c3593ec080755de6&format=json&page=" + numOfPages)
    #value = response.json()
    with open('backend/sample.json') as json_file:
        value = json.load(json_file)
    trackNo = random.randint(0, len(value["tracks"]["track"]))

    songName = value["tracks"]["track"][trackNo]["name"]
    artist = value["tracks"]["track"][trackNo]["artist"]["name"]

    print(songName)
    print(artist)
    return (songName,artist)

#code to store response as a json, use so u dont have to call api multiple times
# # Opening JSON file
# with open('sample.json', 'w') as openfile:
#     json.dump(value, openfile)






