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
