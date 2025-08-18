import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error

# 1. Load dataset
df = pd.read_csv("housing.csv")  # Your dataset with 'MEDV' as target

print("Dataset Head:\n", df.head())

# 2. Features (X) and Target (y)
X = df.drop("MEDV", axis=1)
y = df["MEDV"]

# 3. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Initialize models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

# 5. Evaluate each model
results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    
    r2 = r2_score(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)
    
    results.append({
        "Model": name,
        "R² Score": r2,
        "MSE": mse,
        "RMSE": rmse
    })
    
    print(f"\n{name} Results:")
    print(f"  R² Score: {r2:.2f}")
    print(f"  MSE: {mse:.2f}")
    print(f"  RMSE: {rmse:.2f}")

# 6. Convert results to DataFrame
results_df = pd.DataFrame(results)

# 7. Plot the R² scores
plt.figure(figsize=(8, 5))
plt.bar(results_df["Model"], results_df["R² Score"], color=['orange', 'blue', 'green'])
plt.title("Model Comparison (R² Score)")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.ylim(0, 1)
plt.grid(axis="y")
plt.show()
