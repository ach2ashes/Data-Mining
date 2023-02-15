#get data from a public api https://api.football-data.org/
import json

import requests 
seasons= [2022,2021,2020]
for i in seasons:
    url = "http://api.football-data.org/v4/competitions/PL/matches?season={}".format(i) 
    headers = {'X-Auth-Token': 'd6b7efc4e021470bb64234090447b6c8'} 
    response = requests.get(url, headers=headers) 
    data = response.json() 
    with open('data.json', 'a') as outfile: 
        json.dump(data , outfile,indent=0)
