import pandas as pd
import numpy as np
# Load CSV file
df = pd.read_csv("data.csv")  # Make sure your file name is correct

# Show first 5 records
print("\n📌 First 5 Rows (head):")
print(df.head())

# Show last 5 records
print("\n📌 Last 5 Rows (tail):")
print(df.tail())

# Sorting by Age (Ascending)
print("\n🔽 Sort by Age (Low → High):")
print(df.sort_values(by="Age"))

# Sorting by Salary (Descending)
print("\n🔼 Sort by Salary (High → Low):")
print(df.sort_values(by="Salary", ascending=False))


# NumPy Salary Mean (same result, using NumPy)
salary_np = np.array(df["Salary"])
print("✅ Average Salary (NumPy):", np.mean(salary_np))