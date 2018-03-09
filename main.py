import pandas as pd

##########################################
#                                        #
#             STACKOVERFLOW              #
#                                        #
##########################################

df = pd.read_csv('stackoverflow.csv')

# Count countries
countryCount = {}
for i in df['Country']:
    try:
        countryCount[i] += 1
    except KeyError:
        countryCount[i] = 1

# Eliminate non-relevent countries
for key, value in countryCount.items():
    if(value < 10):
        df = df[df.Country != key]
