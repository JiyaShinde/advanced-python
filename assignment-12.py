import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Load dataset
df = pd.read_csv("customer_churn.csv")

# Display first few records
print(df.head())
print(df.info())
print(df.columns)

# Descriptive statistics
print(df.describe())
print("Mean:\n", df.mean(numeric_only=True))
print("Median:\n", df.median(numeric_only=True))
print("Mode:\n", df.mode().iloc[0])
print("Variance:\n", df.var(numeric_only=True))
print("Standard Deviation:\n", df.std(numeric_only=True))

# Data visualization
df.hist(figsize=(10, 8))
plt.show()

sns.boxplot(data=df.select_dtypes(include="number"))
plt.show()

sns.scatterplot(x="tenure", y="MonthlyCharges", data=df)
plt.show()

# Correlation heatmap
corr = df.select_dtypes(include="number").corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

# Handle missing values
print(df.isnull().sum())
df = df.dropna()

# Detect outliers using Z-score
numeric_df = df.select_dtypes(include="number")
z_scores = numeric_df.apply(zscore)

outliers = (z_scores.abs() > 3)
print("Outliers:\n", df[outliers.any(axis=1)])

# Remove outliers
df = df[~outliers.any(axis=1)]

# Verify cleaned dataset
print(df.isnull().sum())
print(df.head())

# Save cleaned dataset
df.to_csv("cleaned_customer_churn.csv", index=False)
