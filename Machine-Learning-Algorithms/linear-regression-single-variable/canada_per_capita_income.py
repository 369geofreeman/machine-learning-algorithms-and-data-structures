# In this file we predict the income per capita for Canada in 2020 using data from 1971-2016.

import pandas as pd
import numpy as np
from sklearn import linear_model


df = pd.read_csv('canada_per_capita_income.csv')

reg = linear_model.LinearRegression()
reg.fit(df[['year']], df[ 'per capita income (US$)' ])

predict_date = 2020

prediction = reg.predict([[predict_date]])
print('The predicted income per capita for Canada in USD is ${}'.format(prediction))
