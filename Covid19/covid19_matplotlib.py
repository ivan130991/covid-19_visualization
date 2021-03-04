from folium.map import Tooltip
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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