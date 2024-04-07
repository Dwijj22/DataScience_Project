import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Tucson_Police_Reported_Crimes.csv')

# Explore the data
print('----------------------HEAD--------------------------')
print(df.head())

# Check the data types and missing values
print('----------------------INFO--------------------------')
print(df.info())

# Summarize statistics
print('----------------------DESCRIBE--------------------------')
print(df.describe())

# Data Cleaning and Preprocessing
# Convert 'DateOccured' column to datetime format
df['DateOccurred'] = pd.to_datetime(df['DateOccurred'])

#Drop irrelevant columns
df.drop(columns=['ESRI_OID'], inplace=True)

# Check for missing values
print('----------------------MISSING VALUES--------------------------')
print(df.isnull().sum())

# Exploratory Data Analysis (EDA): Conducting eda to uncover patterns in the
# data. Visualize the distribution of crime types.

# Visualize the distribution of crime types
plt.figure(figsize=(10, 6))
sns.countplot(x='UCRDescription', data=df)
plt.xticks(rotation=45, ha='right')
plt.title('Distribution of Crime Types')
plt.show()

# Visualize trends over time
df['YearMonth'] = df['DateOccurred'].dt.to_period('M')
plt.figure(figsize=(10, 6))
sns.countplot(x='YearMonth', data=df)
plt.xticks(rotation=45, ha='right')
plt.title('Number of Crimes Over Time')
plt.show()

# Visualize geographical patterns
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Division', y='Ward', data=df, hue='UCRDescription')
plt.title('Geographical Distribution of Crimes')
plt.show()

# # Create new features or extract relevant info from columns
# df['DayOfWeek'] = df['DateOccurred'].dt.day_name()

# # One-hot encode categorical variables
# df_encoded = pd.get_dummies(df, columns=['Division', 'DayOfWeek'])

# # Drop non-numeric columns
# non_numeric_cols = ['UCRDescription', 'DateOccurred', 'YearMonth']
# df_numeric = df_encoded.drop(columns=non_numeric_cols)

# # Correlation analysis
# correlation_matrix = df_numeric.corr()
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.show()

# # Time series analysis
# crime_by_month = df.groupby('YearMonth').size()
# crime_by_month.plot(figsize=(10, 6))
# plt.title('Number of Crimes Over Time')
# plt.xlabel('Year-Month')
# plt.ylabel('Number of Crimes')
# plt.show()
