# Weather Data Visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load dataset
data = pd.read_csv('weather_data.csv')

# Step 2: Display basic info
print("Weather Data Overview:")
print(data.head())
print("\nSummary Statistics:\n", data.describe())

# Step 3: Line Plot – Temperature over time
plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Temperature'], marker='o', linestyle='-', color='b')
plt.title('Temperature Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 4: Bar Plot – Precipitation
plt.figure(figsize=(10,5))
sns.barplot(x='Date', y='Precipitation', data=data, color='skyblue')
plt.title('Daily Precipitation Levels')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 5: Scatter Plot – Temperature vs Humidity
plt.figure(figsize=(8,5))
sns.scatterplot(x='Temperature', y='Humidity', data=data, color='red', s=80)
plt.title('Temperature vs Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.tight_layout()
plt.show()

# Step 6: Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Between Weather Parameters')
plt.tight_layout()
plt.show()
