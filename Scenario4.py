print("Swasthika M 24BAD121")
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("marketing_campaign.csv", sep="\t")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df["Age"] = 2026 - df["Year_Birth"]
plt.hist(df["Age"], bins=10)
plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.show()
plt.boxplot(df["Income"].dropna())
plt.title("Income Distribution of Customers")
plt.ylabel("Income") 
plt.show()
