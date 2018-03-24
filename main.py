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
print("Top five JavaScript countries :")
print(countries[:5])
#plt.show()

##########################################
#                                        #
#               HAPPINESS                #
#                                        #
##########################################

df = pd.read_csv('stackoverflow.csv')
dfFiltered = pd.DataFrame()
dfHappiness = pd.read_excel('hapiness.xlsx', sheet_name="Figure2.2 WHR 2017")
df = df.merge(dfHappiness, left_on='Country', right_on='Country')
df = df.sort_values(by=['Happiness score'], ascending=False)
df = df.reset_index(drop=True)
bestCountry = df.at[0, "Country"]
print("The country where people are the most happy is : ")
print(df.at[0, "Country"], " with ", df.at[0, "Happiness score"])
bestScore = df.at[0, "Happiness score"]
df = df[df.Country.str.contains(bestCountry)]
print("There is ", len(df), " answers for ", bestCountry)
total = len(df)
df = df[pd.notnull(df['HaveWorkedLanguage'])]
dfFiltered = df[df.HaveWorkedLanguage.str.contains('JavaScript')]
print("There is ", len(dfFiltered), " JavaScripters in ", bestCountry)
print(total - len(dfFiltered), " don't like JavaScript :(")
print("The average salary for ", bestCountry, " is ", df["Salary"].mean())
print("The average JavaScript salary for ", bestCountry, " is ", dfFiltered["Salary"].mean())
print("The distribution for all techs in ", bestCountry)
df = df.sort_values(by=['Salary'])
df = df.reset_index(drop=True)
df = df["Salary"]
df.plot.hist(bins=50)
#plt.show()
print("The distribution in JavaScript for ", bestCountry)
dfFiltered = dfFiltered.sort_values(by=['Salary'])
dfFiltered = dfFiltered.reset_index(drop=True)
dfFiltered = dfFiltered["Salary"]
dfFiltered.plot.hist(bins=50)
#plt.show()
frenchScore = dfHappiness.loc[dfHappiness['Country'] == "France", "Happiness score"].item()
print("France score is ", frenchScore, " so ", bestCountry, "is ", bestScore - frenchScore, " points above.")
