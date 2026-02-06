import pandas as pd
import matplotlib.pyplot as plt
print("Name: Swasthika M")
print("Roll No: 24BAD121")


df = pd.read_csv("diabetes.csv")

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

print(df.isnull().sum())

plt.figure()
plt.hist(df["Glucose"], bins=20)
plt.xlabel("Glucose Level")
plt.ylabel("Frequency")
plt.title("Glucose Level Distribution")
plt.show()

plt.figure()
plt.hist(df["Age"], bins=20)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()

plt.figure()
plt.boxplot(df["Glucose"])
plt.ylabel("Glucose Level")
plt.title("Boxplot of Glucose Levels")
plt.show()

plt.figure()
plt.boxplot(df["Age"])
plt.ylabel("Age")
plt.title("Boxplot of Age")
plt.show()
