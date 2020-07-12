import requests
import pandas
import matplotlib.pyplot as plt
import json

districts_daily = requests.get('https://api.covid19india.org/districts_daily.json')
districts_daily = districts_daily.text
districts_daily = json.loads(districts_daily)
states = []; districts = []; dates = []; active = []; confirmed = []
deceased = []; recovered = []
for state in districts_daily["districtsDaily"]:
    for district in districts_daily["districtsDaily"][state]:
        for day in districts_daily["districtsDaily"][state][district]:
            states.append(state)
            districts.append(district)
            dates.append(day['date'])
            active.append(day['active'])
            confirmed.append(day['confirmed'])
            deceased.append(day['deceased'])
            recovered.append(day['recovered'])
df = pandas.DataFrame({'state': states, 'district': districts, 'active': active, 'confirmed': confirmed, 
                       'recovered': recovered, 'deceased': deceased, 'date': dates})
df['date'] = pandas.to_datetime(df['date'], format = '%Y-%m-%d')
df['active'] = df['active'].astype(int)
df['recovered'] = df['recovered'].astype(int)
df['deceased'] = df['deceased'].astype(int)
df['confirmed'] = df['confirmed'].astype(int)

df.to_csv("C:/Users/0295s/Desktop/districtsdaily.csv")
