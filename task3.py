import pandas as pd

file_path = 'covid_19_clean.csv'
data = pd.read_csv(file_path)

data['Date'] = pd.to_datetime(data['Date'])
june_first_data = data[data['Date'] == '2020-06-01']


total_deaths = june_first_data['Deaths'].sum()


mean_confirmed_cases = june_first_data['Confirmed'].mean()


western_pacific_countries = june_first_data[
    (june_first_data['WHO Region'] == 'Western Pacific') & 
    (june_first_data['Confirmed'] > mean_confirmed_cases)
]
print(total_deaths)
print(western_pacific_countries['Country/Region'])
