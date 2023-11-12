import matplotlib.pyplot as plt
import pandas as pd

# Load your data (replace 'data.csv' with your data file)
data = pd.read_csv('data.csv')

# Explore the data
print(data.head())  # Display the first few rows of the data

# Create a basic plot
plt.figure(figsize=(8, 6))
plt.scatter(data['X'], data['Y'])
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()