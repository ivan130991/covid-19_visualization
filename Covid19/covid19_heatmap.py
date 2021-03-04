from datetime import date
from folium.map import Tooltip
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import folium
import json

###PULL COVID-19 DATA
database = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

###DATA CLEANING
database = database.fillna(0)
database = database[database['iso_code'] != 0]
database = database[database['iso_code'] != 'OWID_WRL']
database = database[database['iso_code'] != 'OWID_KOS']

###PLOT ON WORLD MAP
latest_avail_data = database.groupby(['iso_code'])['new_cases'].sum()
latest_avail_data = np.log(latest_avail_data)
latest_avail_data[latest_avail_data == -np.inf] = 0
latest_avail_data = latest_avail_data.to_frame()
latest_avail_data = latest_avail_data.reset_index()

world_map = folium.Map(location = (0, 0), zoom_start=2)
country_geo = r'..\geo-countries\data\countries.geojson'
with open(country_geo, encoding="utf-8") as f:
    map_data = json.load(f)
    for item in map_data['features']:
        item['properties']['tooltip1'] = item['properties']['ADMIN']
        for idx in latest_avail_data['iso_code']:
            if idx == item['properties']['ISO_A3']:
                item_count = latest_avail_data[latest_avail_data['iso_code'] == idx]['new_cases'].values
                item['properties']['tooltip1'] = item['properties']['tooltip1'] + ' ' + np.array2string(item_count, precision = 2)
base_map = folium.Choropleth(geo_data = map_data, data = latest_avail_data, columns = ['iso_code', 'new_cases'],key_on = 'feature.properties.ISO_A3',fill_color='YlGnBu', fill_opacity = 0.7, line_opacity = 0.2, legend_name = 'Total Covid Cases in log scale')
base_map.add_to(world_map)
base_map.geojson.add_child(folium.GeoJsonTooltip(['tooltip1'], labels = False))

world_map.save('../covid-19_visualization/Covid19/world_map_{}.html'.format(date.today()))