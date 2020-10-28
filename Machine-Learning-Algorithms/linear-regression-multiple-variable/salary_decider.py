# A script that uses multivariable linear regression to predict the correct
# salary for a new employee based on his experience, test score (out of 10) 
# and interview score (out of 10)


import numpy as np
import pandas as pd
from sklearn import linear_model
import math


df = pd.read_csv('hiring.csv')


# Fit the empty data slots

median_test_scores = math.floor(df['test_score(out of 10)'].median() )
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(median_test_scores)


# Convert string number to int

nums = {'NaN':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11}

print(df.experience[2])

for i,v in enumerate(df.experience):
    if df.experience[i] in nums.keys(): df.experience[i] = nums[v]
    else: df.experience[i] = 0


# create our linear regression class object

reg = linear_model.LinearRegression()


# train the model


reg.fit(df[['experience', 'test_score(out of 10)', 'interview_score(out of 10)']], df['salary($)'])


# Predictions


# candidate 1: 
    # Experience: 2 years
    # Test score: 9
    # Interview score: 6


prediction1 = reg.predict([[2, 9, 6]])


# Candidate 2:
    # Experience: 12 years
    # Test score: 10
    # Interview score: 10

prediction2 = reg.predict([[12, 10, 10]])


# Print the results

print('\n'*5)
print('Applicant one has 2 years experience, scored 9 on the test and a 6 in the interview...')
print('Their salary is estimated to be: £{}'.format(round(float(prediction1), 2)))
print('\n')
print('Applicant two has 12 years experience, scored 10 on the test and a 10 in the interview...')
print('Their salary will be: £{}'.format(round(float(prediction2), 2)))






