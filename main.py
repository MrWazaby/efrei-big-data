import pandas as pd
import numpy as np

##########################################
#                                        #
#             STACKOVERFLOW              #
#                                        #
##########################################

df = pd.read_csv('stackoverflow.csv')

# Count countries and exclude non-relevent
countries = pd.DataFrame(df.groupby('Country').size())
countries.columns = ['CountryCount']
countries = countries[countries.CountryCount >= 10]
countries = countries.dropna()
countries['Country'] = countries.index
df = df[df.Country.isin(countries.Country)]

# Select only JavaScript
df = df[pd.notnull(df['HaveWorkedLanguage'])]
df = df[df.HaveWorkedLanguage.str.contains('JavaScript')]
