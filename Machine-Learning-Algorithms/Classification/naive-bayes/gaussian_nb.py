from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

# Assigning features and label variables
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']


# create label encoder
le = preprocessing.LabelEncoder()
# Convert string labels into numbers
weather_encoded = le.fit_transform(weather)
temp_encoded = le.fit_transform(temp)
label = le.fit_transform(play)


print('Temp', temp_encoded)
print('Play:', label)
print('Weather', weather_encoded)



# Combining weather and temp into a single list of tuples
features = [list(i) for i in zip(weather_encoded, temp_encoded)]

# Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the traning sets
model.fit(features, label)

# Predict the output
predicted = model.predict([[0, 2]])  # 0: overcast, 2: mild

print('Predicted Value', predicted)

