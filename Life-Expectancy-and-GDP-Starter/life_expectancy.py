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

# we can extract the data for a specific country
usa_data = df[df['Country'] == 'United States of America']
china_data = df[df['Country'] == 'China']
germany_data = df[df['Country'] == 'Germany']
chile_data = df[df['Country'] == 'Chile']
mexico_data = df[df['Country'] == 'Mexico']
zimbabwe_data = df[df['Country'] == 'Zimbabwe']

# let's look at the life expectancy over time for our countries. Zimbawe is an outlier, so we will give it a separate plot
plt.plot(usa_data['Year'], usa_data['Life expectancy at birth (years)'], label='United States')
plt.plot(china_data['Year'], china_data['Life expectancy at birth (years)'], label='China')
plt.plot(germany_data['Year'], germany_data['Life expectancy at birth (years)'], label='Germany')
plt.plot(chile_data['Year'], chile_data['Life expectancy at birth (years)'], label='Chile')
plt.plot(mexico_data['Year'], mexico_data['Life expectancy at birth (years)'], label='Mexico')

plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Life Expectancy Over Time')
plt.legend()
# plt.show()
plt.clf()

plt.plot(zimbabwe_data['Year'], zimbabwe_data['Life expectancy at birth (years)'], label='Zimbabwe')
plt.plot(usa_data['Year'], usa_data['Life expectancy at birth (years)'], label='United States')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.title('Life Expectancy Over Time (Zimbabwe vs USA)')
plt.legend()
# plt.show()
plt.clf()

#Let's now look at the evolution of GDP per capita over time for our countries. We will use subplots
plt.subplot(2, 3, 1)
plt.title('Usa')
plt.plot(usa_data['Year'], usa_data['GDP'])
plt.subplot(2, 3, 2)
plt.title('China')
plt.plot(china_data['Year'], china_data['GDP'])
plt.subplot(2, 3, 3)
plt.title('Germany')
plt.plot(germany_data['Year'], germany_data['GDP'])
plt.subplot(2, 3, 4)
plt.title('Chile')
plt.plot(chile_data['Year'], chile_data['GDP'])
plt.subplot(2, 3, 5)
plt.title('Mexico')    
plt.plot(mexico_data['Year'], mexico_data['GDP'])
plt.subplot(2, 3, 6)
plt.title('Zimbabwe')
plt.plot(zimbabwe_data['Year'], zimbabwe_data['GDP'])
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.xlabel('Year')
plt.ylabel('GDP per Capita')
# plt.show()
plt.clf()

plt.plot(usa_data['Year'], usa_data['GDP'], label='United States')
plt.plot(china_data['Year'], china_data['GDP'], label='China')
plt.plot(germany_data['Year'], germany_data['GDP'], label='Germany')
plt.plot(chile_data['Year'], chile_data['GDP'], label='Chile')
plt.plot(mexico_data['Year'], mexico_data['GDP'], label='Mexico')
plt.plot(zimbabwe_data['Year'], zimbabwe_data['GDP'], label='Zimbabwe')
plt.xlabel('Year')
plt.ylabel('GDP per Capita')
plt.title('GDP per Capita Over Time')
plt.legend()
# plt.show()
plt.clf()

# let's look at the relationship between GDP per capita and life expectancy for our countries. We will use scatter plots
plt.subplot(2, 3, 1)
plt.scatter(usa_data['GDP'], usa_data['Life expectancy at birth (years)'], label='United States')
plt.title('USA')
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.subplot(2, 3, 2)
plt.scatter(china_data['GDP'], china_data['Life expectancy at birth (years)'], label='China')
plt.title('China')
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.subplot(2, 3, 3)
plt.scatter(germany_data['GDP'], germany_data['Life expectancy at birth (years)'], label='Germany')
plt.title('Germany')
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.subplot(2, 3, 4)
plt.scatter(chile_data['GDP'], chile_data['Life expectancy at birth (years)'], label='Chile')
plt.title('Chile')
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.subplot(2, 3, 5)
plt.scatter(mexico_data['GDP'], mexico_data['Life expectancy at birth (years)'], label='Mexico')
plt.title('Mexico')
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.subplot(2, 3, 6)
plt.scatter(zimbabwe_data['GDP'], zimbabwe_data['Life expectancy at birth (years)'], label='Zimbabwe')
plt.title('Zimbabwe')
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.show()
