from sklearn.linear_model import LinearRegression

# Sample training data
X = [[20], [22], [24], [26], [28]]
y = [55, 60, 65, 70, 75]

# Create a model
model = LinearRegression()

# Fit the model
model.fit(X, y)

# Predict (example)
prediction = model.predict([[30]])
print("Predicted value for 30:", prediction[0])
