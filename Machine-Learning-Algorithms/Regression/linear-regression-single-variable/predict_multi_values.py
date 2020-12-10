# This is a file that will load in a CSV file with multiple houses sqft area sizes and we will predict the house price for each of them 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Load in the CSV file contaning the area sizes and the traning set 
d = pd.read_csv("areas.csv")
df = pd.read_csv('homeprices.csv')

# train our model
reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)

# Predict our prices
p = reg.predict(d)

# Assign a new column on the dataframe
d['Prices'] = p

# Print data frame to see the predicted prices against the area sizes

print(d)


# Write the results a fresh csv file

d.to_csv('Prediction.csv', index=False)

