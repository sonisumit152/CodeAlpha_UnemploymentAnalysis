import zipfile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Extract ZIP File
with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Load Dataset
df = pd.read_csv('Unemployment in India.csv')

# Data Cleaning
df.columns = df.columns.str.strip()
df.dropna(inplace=True)

# Convert Date Column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Dataset Preview
display(df.head())

# Dataset Information
df.info()

# Statistical Summary
display(df.describe())

# Distribution of Unemployment Rate
plt.figure(figsize=(10,5))
sns.histplot(df['Estimated Unemployment Rate (%)'], bins=20, kde=True)
plt.title('Distribution of Unemployment Rate')
plt.show()

# Region-wise Unemployment Analysis
region_unemployment = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False)

plt.figure(figsize=(12,6))
region_unemployment.head(10).plot(kind='bar')
plt.title('Top 10 Regions by Average Unemployment Rate')
plt.xlabel('Region')
plt.ylabel('Average Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.show()

# Covid-19 Impact Analysis
covid_period = df[df['Date'] >= '2020-03-01']

plt.figure(figsize=(12,6))
sns.lineplot(
    x='Date',
    y='Estimated Unemployment Rate (%)',
    data=covid_period
)

plt.title('Impact of Covid-19 on Unemployment Rate')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.show()

# Key Insights
print("Key Insights")
print("1. Unemployment rates varied significantly across regions.")
print("2. Covid-19 increased unemployment levels in many states.")
print("3. Significant regional differences were observed.")
print("4. Visualization helped identify major employment trends.")
