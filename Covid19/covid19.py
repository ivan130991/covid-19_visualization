import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import math

###PULL COVID-19 DATA
database = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

###DATA CLEANING
database = database.fillna(0)
database = database[database['iso_code'] != 0]
database = database[database['iso_code'] != 'OWID_WRL']
database = database[database['iso_code'] != 'OWID_KOS']

###RANK COUNTRIES ACCORDING TO TOTAL NUMBER OF POSITIVE CASES
total_cases = database.groupby(['location'])['new_cases'].sum()
total_cases = total_cases.sort_values(ascending = False)
total_cases.head(25).plot(kind = 'bar', subplots = True)
plt.xlabel('Country')
plt.xticks(rotation = 45)
plt.ylabel('Number of Positive Cases')
plt.title('Total Number of Positive Covid-19 Cases as at {}'.format(database['date'].max()))
plt.show()

###RANK COUNTRIES ACCORDING TO TOTAL NUMBER OF POSITIVE CASES PER MILLION
total_cases_per_mil = database.groupby(['location'])['new_cases_per_million'].sum()
total_cases_per_mil = total_cases_per_mil.sort_values(ascending = False)
total_cases_per_mil.head(25).plot(kind = 'bar', subplots = True)
plt.xlabel('Country')
plt.xticks(rotation = 45)
plt.ylabel('Number of positive cases per million population')
plt.title('Total Number of Positive Covid-19 cases per million population as at {}'.format(database['date'].max()))
plt.show()

###RANK COUNTRIES ACCORDING TO THE TOTAL NUMBER OF DEATHS
total_deaths = database.groupby(['location'])['new_deaths'].sum()
total_deaths = total_deaths.sort_values(ascending = False)
total_deaths.head(25).plot(kind = 'bar', subplots = True)
plt.xlabel('Country')
plt.xticks(rotation = 45)
plt.ylabel('Number of deaths')
plt.title('Total Number of confirmed Covid-19 Deaths as at{}'.format(database['date'].max()))
plt.show()

###RANK COUNTRIES ACCORDING TO THE TOTAL NUMBER OF DEATHS PER MILLION
total_deaths_per_mil = database.groupby(['location'])['new_deaths_per_million'].sum()
total_deaths_per_mil = total_deaths_per_mil.sort_values(ascending = False)
total_deaths_per_mil.head(25).plot(kind = 'bar', subplots = True)
plt.xlabel('Country')
plt.xticks(rotation = 45)
plt.ylabel('Number of deaths per million population')
plt.title('Number of deaths per million population as at {}'.format(database['date'].max()))
plt.show()

###RANK COUNTRIES ACCORDING TO TOTAL NUMBER OF DEATHS OVER TOTAL NUMBER OF POSITIVE CASES
proportion = (total_deaths/total_cases)*100
proportion = proportion.sort_values(ascending = False)
proportion.head(25).plot(kind = 'bar', subplots = True)
plt.xlabel('Country')
plt.xticks(rotation = 45)
plt.ylabel('Proportion of deaths over cases')
plt.title('Proportion of deaths over positive cases as at {}'.format(database['date'].max()))
plt.show()

###PLOT ON WORLD MAP
latest_avail_data = database.groupby(['iso_code'])['new_cases'].sum()
print(latest_avail_data)
world_map = folium.Map(location = [100, 0], zoom_start = 1.5)
country_geo = '..\covid-19_visualization\Covid19\world-countries.json'
folium.Choropleth(geo_data = country_geo, data = latest_avail_data, columns = ['iso_code', 'new_cases'],key_on = 'feature.id',fill_color='YlGnBu', fill_opacity = 0.7, line_opacity = 0.2, legend_name = 'Total Covid Cases').add_to(world_map)
world_map.save('../covid-19_visualization/Covid19/world_map.html')