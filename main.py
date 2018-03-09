import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##########################################
#                                        #
#             STACKOVERFLOW              #
#                                        #
##########################################

df = pd.read_csv('stackoverflow.csv')
baseSize = len(df);

print(baseSize, "rows imported.")

# Count countries and exclude non-relevent
print("Filtering by countries...")
countries = pd.DataFrame(df.groupby('Country').size())
countries.columns = ['CountryCount']
countries = countries[countries.CountryCount >= 10]
countries = countries.dropna()
countries['Country'] = countries.index
df = df[df.Country.isin(countries.Country)]
print(baseSize - len(df), "rows filtered. (", len(df), "rows )");
baseSize = len(df)

# Select only JavaScript
print("Filtering by languages (JavaScript)...")
df = df[pd.notnull(df['HaveWorkedLanguage'])]
df = df[df.HaveWorkedLanguage.str.contains('JavaScript')]
print(baseSize - len(df), "rows filtered. (", len(df), "rows )");
baseSize = len(df)

# Generate graph
countries = pd.DataFrame(df.groupby('Country').size())
countries.columns = ['CountryCount']
countries = countries.sort_values(['CountryCount'], ascending=False)
countries.plot(kind='bar')
plt.show()
