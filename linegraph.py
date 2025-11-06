import matplotlib.pyplot as plt

# Sample data for line graph
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 170, 200, 220]
# Create Line Graph
plt.figure()
plt.plot(months, sales)  # No specific colors
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Growth")
plt.grid(True)  # Optional: for better readability
plt.show()
