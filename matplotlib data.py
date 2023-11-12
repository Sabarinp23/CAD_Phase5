import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013, 2014, 2015]
revenue = [100, 120, 150, 200, 180, 250]

# Create a line chart
plt.figure(figsize=(8, 6))  # Optional: Adjust the figure size
plt.plot(years, revenue, marker='o', linestyle='-', color='b', label='Revenue')
plt.title('Revenue Trends Over the Years')
plt.xlabel('Year')
plt.ylabel('Revenue (in millions)')
plt.grid(True)
plt.legend()
plt.show()