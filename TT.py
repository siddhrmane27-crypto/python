import pandas as pd
import random

# Sample dataset
data = {
    'Age': [20, 22, 24, 26, 28, 30, 32, 34],
    'Height': [5.1, 5.7, 6.0, 5.5, 6.2, 5.8, 6.1, 6.3],
    'Weight': [55, 60, 65, 70, 75, 80, 85, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Shuffle the DataFrame rows
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Define train-test split ratio
split_ratio = 0.8
split_index = int(len(df) * split_ratio)

# Split into train and test sets
train_df = df[:split_index]
test_df = df[split_index:]

# Separate features (X) and target (y)
X_train = train_df[['Age', 'Height']]
y_train = train_df['Weight']

X_test = test_df[['Age', 'Height']]
y_test = test_df['Weight']

# Show output
print("X_train:\n", X_train)
print("\nX_test:\n", X_test)
print("\ny_train:\n", y_train)
print("\ny_test:\n", y_test)
