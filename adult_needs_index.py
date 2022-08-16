# -*- coding: utf-8 -*-
"""Adult Needs Index.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xe1JuEVVbuJ5csUDZLmgarjo3OSozIv0

This Code imports multiple packages for api usage
"""

from google.colab import files # allows for file upload and download

import pandas as pd #Statisitical manipulation
import numpy as np # additional manipulations
import seaborn as sns # Data Visualization
import matplotlib as plt # Additional Data Visualization
import requests as rq # Allows for census api to be used

!pip install rtree

!pip install pygeos
!pip install geopandas # pip install geopandas



import geopandas as gpd # import geopandas

import rtree

import pygeos

api_key= '' # Census API Key found here https://api.census.gov/data/key_signup.html

# set conditions of api key variables
year='2020'
dsource='acs'
dname='acs5'
cols='B25070_001E,B25070_007E,B25070_008E,B25070_009E,B25070_010E,B28001_001E,B28001_011E,B28002_013E,B19058_001E,B19058_002E,B23001_002E' # selects the number of heads of hosueholds and the number of householders in rent occup
state='42'
county = 101
tract = 141

base_url = f'https://api.census.gov/data/{year}/{dsource}/{dname}'
data_url = f'{base_url}?get={cols}&for=tract:*&in=county:{county}&in=state:{state}&key={api_key}'
response= rq.get(data_url)
response = response.json()
response=pd.DataFrame(response[1:], columns=response[0])
response['Census Tract Name'] = response['tract'].astype(float)/100
response.iloc[:,0:10] = response.iloc[:,0:10].astype(float)
response['Total Rent Burdened'] = response.iloc[:, 1:5].sum(axis = 1)
response['Total Low Computer/Internet Access'] = response.iloc[:, 7:8].sum(axis = 1)
response['Percent Rent Burdened'] = response['Total Rent Burdened']/response['B25070_001E']
response['Percent of people Without Computer or Internet Access'] = response['Total Low Computer/Internet Access']/response['B28001_001E']
response['Percent of Households Receiving SNAP'] = response['B19058_002E']/response['B19058_001E']
response

year='2020'
dsource='acs'
dname='acs5'
cols='B23001_003E,B23001_010E,B23001_017E,B23001_024E,B23001_031E,B23001_038E,B23001_045E,B23001_052E,B23001_059E,B23001_066E' # selects the total male workforce between 18 and 65
state='42'
county = 101
tract = 141

base_url = f'https://api.census.gov/data/{year}/{dsource}/{dname}'
data_url = f'{base_url}?get={cols}&for=tract:*&in=county:{county}&in=state:{state}&key={api_key}'
m_totalpop= rq.get(data_url)
m_totalpop = m_totalpop.json()
m_totalpop=pd.DataFrame(m_totalpop[1:], columns=m_totalpop[0])
m_totalpop.iloc[:,0:10] = m_totalpop.iloc[:, 0:10].astype(float)
m_totalpop['Total Male Workforce'] = m_totalpop.iloc[:, 0:10].sum(axis = 1)
m_totalpop

year='2020'
dsource='acs'
dname='acs5'
cols='B23001_008E,B23001_015E,B23001_022E,B23001_029E,B23001_036E,B23001_043E,B23001_050E,B23001_057E,B23001_064E,B23001_071E' # selects the number of men who are unemployed
state='42'
county = 101
tract = 141

base_url = f'https://api.census.gov/data/{year}/{dsource}/{dname}'
data_url = f'{base_url}?get={cols}&for=tract:*&in=county:{county}&in=state:{state}&key={api_key}'
m_unemployed= rq.get(data_url)
m_unemployed = m_unemployed.json()
m_unemployed=pd.DataFrame(m_unemployed[1:], columns=m_unemployed[0])
m_unemployed.iloc[:,0:10] = m_unemployed.iloc[:, 0:10].astype(float)
m_unemployed['Total Male Unemployed Workforce'] = m_unemployed.iloc[:, 0:10].sum(axis = 1)
m_unemployed['Percent Unemployed'] = m_unemployed['Total Male Unemployed Workforce'] / m_totalpop['Total Male Workforce']
response['Total Male Unemployed'] = m_unemployed['Total Male Unemployed Workforce']
response['Percent Male Unemployed'] = m_unemployed['Percent Unemployed']
response

year='2020'
dsource='acs'
dname='acs5'
cols='B01001_002E,B01001_026E,B06009_002E' #Selects the number of children under the age of 5
state='42'
county = 101
tract = 141

base_url = f'https://api.census.gov/data/{year}/{dsource}/{dname}'
data_url = f'{base_url}?get={cols}&for=tract:*&in=county:{county}&in=state:{state}&key={api_key}'
child_demand= rq.get(data_url)
child_demand = child_demand.json()
child_demand=pd.DataFrame(child_demand[1:], columns=child_demand[0])
child_demand.iloc[:,0:2] = child_demand.iloc[:, 0:2].astype(float)
response['Number of Children Under 5'] = child_demand.iloc[:, 0:2].sum(axis = 1)
response

year='2020'
dsource='acs'
dname='acs5'
cols='B06009_001E,B06009_002E' #Selects the number of people without a high school diploma
state='42'
county = 101
tract = 141

base_url = f'https://api.census.gov/data/{year}/{dsource}/{dname}'
data_url = f'{base_url}?get={cols}&for=tract:*&in=county:{county}&in=state:{state}&key={api_key}'
child_demand= rq.get(data_url)
child_demand = child_demand.json()
child_demand=pd.DataFrame(child_demand[1:], columns=child_demand[0])
child_demand.iloc[:,0:2] = child_demand.iloc[:, 0:2].astype(float)
child_demand['B06009_001E'] = child_demand['B06009_001E'].replace(0,1)
child_demand['Percent Without High School Diploma'] = child_demand['B06009_002E']/child_demand['B06009_001E']
response['Percent Without a High School Diploma'] = child_demand['Percent Without High School Diploma']
response['Total Without a High School Diploma'] = child_demand['B06009_002E']
response

year='2020'
dsource='acs'
dname='acs5'
cols='B06012_001E,B06012_002E' #Selects the number of people living in poverty
state='42'
county = 101
tract = 141

base_url = f'https://api.census.gov/data/{year}/{dsource}/{dname}'
data_url = f'{base_url}?get={cols}&for=tract:*&in=county:{county}&in=state:{state}&key={api_key}'
child_demand= rq.get(data_url)
child_demand = child_demand.json()
child_demand=pd.DataFrame(child_demand[1:], columns=child_demand[0])
child_demand.iloc[:,0:2] = child_demand.iloc[:, 0:2].astype(float)
child_demand
response['Total Snap Eligible'] = child_demand['B06012_002E']
child_demand['B06012_001E'] = child_demand['B06012_001E'].replace(0,1)
response['Percent Snap Eligible'] = child_demand['B06012_002E']/child_demand['B06012_001E']
response

year='2020'
dsource='acs'
dname='acs5'
cols='B06007_001E,B06007_008E' #Selects the number of people living in poverty
state='42'
county = 101
tract = 141

base_url = f'https://api.census.gov/data/{year}/{dsource}/{dname}'
data_url = f'{base_url}?get={cols}&for=tract:*&in=county:{county}&in=state:{state}&key={api_key}'
child_demand= rq.get(data_url)
child_demand = child_demand.json()
child_demand=pd.DataFrame(child_demand[1:], columns=child_demand[0])
child_demand.iloc[:,0:2] = child_demand.iloc[:, 0:2].astype(float)
child_demand
response['Total ESL Adults'] = child_demand['B06007_008E']
child_demand['B06007_001E'] = child_demand['B06007_001E'].replace(0,1)
response['Percent ESL Adults'] = child_demand['B06007_008E']/child_demand['B06007_001E']
response

files.upload() #upload the shootings file information fonud here: https://phl.carto.com/api/v2/sql?q=SELECT+*,+ST_Y(the_geom)+AS+lat,+ST_X(the_geom)+AS+lng+FROM+shootings&filename=shootings&format=csv&skipfields=cartodb_id
# Upload the Census 2020 Shapefiles Found here: https://geo.btaa.org/catalog/dd253c179ac643e3870d31cc0c059d4b_0
#Upload the Philadelphia Neighborhoods found here: https://github.com/azavea/geo-data

from google.colab import drive
drive.mount('/content/drive')

gpd.read_file('Neighborhoods_Philadelphia.geojson')

Shootings = pd.read_csv('Shootings 8.12.22.csv') # Read in shootings data

Shootings['date_'] = pd.to_datetime(Shootings['date_']) # convert shooting data to date

Shootings = Shootings.loc[(Shootings['date_'] >= '2022-01-01')] # Filter Shootings for only 2022

Shootings = gpd.GeoDataFrame(Shootings, geometry=gpd.points_from_xy(Shootings.lng, Shootings.lat), crs="EPSG:4326") # Convert to a geo dataframe

Philadelphia_census_tracts = gpd.read_file("Census_Tracts_2020.shp") # Read in the Census Tracts

Philadelphia_Neighborhoods = gpd.read_file('Neighborhoods_Philadelphia.geojson')

Shootings_Joined = Shootings.sjoin(Philadelphia_census_tracts, how="inner")

Shootings_Joined = pd.DataFrame(Shootings_Joined)

Shooting_count = pd.DataFrame(Shootings_Joined['NAME'].value_counts()).reset_index(level=0)

Shooting_count.rename({'index': 'Census Tract Name', 'NAME': 'Count of Shootings'}, axis=1, inplace=True)

Shooting_count.iloc[:,0:2] = Shooting_count.iloc[:, 0:2].astype(float)

Philadelphia_census_tracts

complete_index = pd.merge(response, Shooting_count, on="Census Tract Name", how="left")



complete_index['Count of Shootings'] = pd.qcut(complete_index['Count of Shootings'], 4, labels = False) + 1
complete_index['Count of Shootings'] = complete_index['Count of Shootings'].fillna(0)
complete_index['Total Rent Burdened'] = pd.qcut(complete_index['Total Rent Burdened'], 4, labels = False) + 1
complete_index['Total Low Computer/Internet Access'] = pd.qcut(complete_index['Total Low Computer/Internet Access'], 4, labels = False) + 1
complete_index['Total Male Unemployed'] = pd.qcut(complete_index['Total Male Unemployed'], 4, labels = False) + 1
complete_index['Total Snap Eligible'] = pd.qcut(complete_index['Total Snap Eligible'], 4, labels = False) + 1
complete_index['Total Without a High School Diploma'] = pd.qcut(complete_index['Total Without a High School Diploma'], 4, labels = False) + 1
complete_index['Percent of Households Receiving SNAP'] = pd.qcut(complete_index['Percent of Households Receiving SNAP'], 4, labels = False) + 1
complete_index['Total ESL Adults'] = pd.qcut(complete_index['Total ESL Adults'], 4, labels = False) + 1
complete_index['Number of Children Under 5'] = pd.qcut(complete_index['Number of Children Under 5'], 4, labels = False) + 1

complete_index['Total Need Index'] = complete_index['Count of Shootings'] + complete_index['Total Rent Burdened'] + complete_index['Total Low Computer/Internet Access'] + complete_index['Total Male Unemployed'] + complete_index['Total Snap Eligible'] + complete_index['Total ESL Adults'] + complete_index['Number of Children Under 5']

complete_index

complete_index.rename({'Census Tract Name': 'NAME'}, axis = 1, inplace = True)
Philadelphia_census_tracts['NAME'] = Philadelphia_census_tracts['NAME'].astype(float)
Adult_Need_Index_Census_Tract = pd.merge(Philadelphia_census_tracts, complete_index, on = 'NAME')

Need_Index_Neighborhood = Philadelphia_Neighborhoods.sjoin(Adult_Need_Index_Census_Tract, predicate = "intersects", how="left")



Need_Index_Neighborhood = Need_Index_Neighborhood.groupby('MAPNAME').mean()

Need_Index_Neighborhood = Need_Index_Neighborhood.reset_index(level=0)

Need_Index_Neighborhood = pd.merge(Need_Index_Neighborhood, Philadelphia_Neighborhoods[['MAPNAME', 'geometry']], on = 'MAPNAME')

Need_Index_Neighborhood

Need_Index_Neighborhood.to_file('Adult Needs Index 2022.shp')