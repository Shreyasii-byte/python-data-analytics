
# ==========================================
# DAY 9: EXPLORATORY DATA ANALYSIS (EDA)
# Objective: Explore retail sales patterns
# Libraries: Pandas, NumPy, Matplotlib, Seaborn
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create sample retail dataset

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Customer": ["Aarav", "Priya", "Riya", "Kabir",
                 "Ananya", "Rahul", "Meera", "Arjun"],
    "City": ["Delhi", "Mumbai", "Delhi", "Bengaluru",
             "Mumbai", "Delhi", "Pune", "Mumbai"],
    "Category": ["Electronics", "Fashion", "Electronics",
                 "Furniture", "Fashion", "Furniture",
                 "Electronics", "Fashion"],
    "Sales": [2500, 1800, 3200, 4500, 3500, 2100, 5800, 2700],
    "Quantity": [2, 1, 3, 2, 2, 1, 4, 2]
}

df = pd.DataFrame(data)

# 2. Basic dataset exploration

print("\n--- DATASET OVERVIEW ---")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

# 3. Check missing values and duplicates

print("\n--- DATA QUALITY CHECK ---")
print("Missing Values:\n", df.isnull().sum())
print("Duplicate Records:", df.duplicated().sum())

# 4. Key performance indicators (KPIs)

print("\n--- SALES KPIs ---")

print("Total Revenue:", df["Sales"].sum())
print("Average Order Value:", round(df["Sales"].mean(), 2))
print("Total Orders:", df["Order_ID"].nunique())
print("Total Quantity:", df["Quantity"].sum())

# 5. Category-wise sales analysis

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- CATEGORY-WISE SALES ---")
print(category_sales)

# 6. City-wise sales analysis

city_sales = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- CITY-WISE SALES ---")
print(city_sales)

# 7. Sales distribution

plt.figure(figsize=(8, 5))
sns.histplot(df["Sales"], bins=5, kde=True)
plt.title("Distribution of Sales")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.show()

# 8. Category-wise revenue visualization

plt.figure(figsize=(8, 5))
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title("Revenue by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# 9. City-wise revenue visualization

plt.figure(figsize=(8, 5))
sns.barplot(x=city_sales.index, y=city_sales.values)
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("city_sales.png")
plt.show()

# 10. Correlation analysis

correlation = df[["Sales", "Quantity"]].corr()

print("\n--- CORRELATION MATRIX ---")
print(correlation)

plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Sales and Quantity Correlation")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# 11. Sales vs Quantity

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Quantity", y="Sales", hue="Category")
plt.title("Sales vs Quantity")
plt.xlabel("Quantity Sold")
plt.ylabel("Sales Amount")
plt.tight_layout()
plt.savefig("sales_vs_quantity.png")
plt.show()

# 12. Final analytical insights

print("\n--- KEY FINDINGS ---")
print("Highest Revenue Category:", category_sales.idxmax())
print("Highest Revenue City:", city_sales.idxmax())
print("Highest Individual Order:", df["Sales"].max())
print("Lowest Individual Order:", df["Sales"].min())

print("\nEDA COMPLETED SUCCESSFULLY!")
