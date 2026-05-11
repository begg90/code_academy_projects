import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# to load our data, we will use the pandas library to read the csv file and store it in a dataframe
df = pd.read_csv('all_data.csv')

# to get a quick overview of our data, we can use the head() method to see the first few rows of the dataframe
print(df.head())

# to get a summary of our data, we can use the describe() method to see the statistical summary of our columns
print(df.describe(include='all'))

# look to unique countries in our dataset
print(df['Country'].unique())

# we can estract the data for a specific country, for example, we can extract the data for 'United States', 'China and 'Germany' to compare their life expectancy and GDP per capita over the years
usa_data = df[df['Country'] == 'United States']
china_data = df[df['Country'] == 'China']
germany_data = df[df['Country'] == 'Germany']
