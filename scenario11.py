import pandas as pd
import matplotlib.pyplot as plt
print("Name: Swasthika M")
print("Roll No: 24BAD121")
print("Introduction to Python Libraries and Dataset Preprocessing")
df = pd.read_csv("data.csv", encoding="latin1")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

print(df.isnull().sum())

sales_per_product = df.groupby("Description")["Quantity"].sum()

plt.figure()
sales_per_product.head(10).plot(kind='bar')
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.title("Sales per Product - Bar Chart")
plt.show()

plt.figure()
sales_per_product.head(10).plot(kind='line', marker='o')
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.title("Sales per Product - Line Chart")
plt.show()
