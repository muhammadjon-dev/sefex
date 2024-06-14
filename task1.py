import json
with open("forecast.json", "r") as f:
    data = json.loads(f.read())
date = '2024-06-10T04:00'
index_of_date = data['hourly']['time'].index(date)
print(data['hourly']['temperature_2m'][index_of_date])
