# SUDHIKSHA 24BAD117
# SCENARIO 3: HOUSING DATA

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Housing.csv")

print(df.columns)
print(df.isnull().sum())

numeric_df = df.select_dtypes(include=["int64", "float64"])

plt.scatter(numeric_df["area"], numeric_df["price"])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price")
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()
