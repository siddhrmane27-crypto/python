import matplotlib.pyplot as plt

# Sample data
height = [150, 155, 160, 165, 170, 175, 180]
weight = [45, 50, 55, 65, 70, 75, 85]

# Create scatter plot
plt.figure()
plt.scatter(height, weight) 
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs Weight Scatter Plot")
plt.grid(True)
plt.show()
