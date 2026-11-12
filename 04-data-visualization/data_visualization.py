
# ==========================================
# DAY 11: DATA VISUALIZATION
# Objective: Visualize retail sales patterns
# Libraries: Pandas, Matplotlib, Seaborn
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create sample sales dataset

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Revenue": [12000, 15000, 13500, 18000, 22000, 25000],
    "Orders": [120, 145, 135, 180, 210, 240],
    "Marketing_Spend": [2000, 2500, 2200, 3000, 3500, 4000]
}

df = pd.DataFrame(data)

sns.set_theme(style="whitegrid")

# 2. Revenue Trend - Line Chart

plt.figure(figsize=(9, 5))
sns.lineplot(data=df, x="Month", y="Revenue", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_trend.png")
plt.show()

# 3. Monthly Orders - Bar Chart

plt.figure(figsize=(9, 5))
sns.barplot(data=df, x="Month", y="Orders")
plt.title("Monthly Order Analysis")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("monthly_orders.png")
plt.show()

# 4. Revenue Distribution - Histogram

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Revenue", bins=5, kde=True)
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig("revenue_distribution.png")
plt.show()

# 5. Marketing Spend vs Revenue - Scatter Plot

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Marketing_Spend",
    y="Revenue",
    s=100
)
plt.title("Marketing Spend vs Revenue")
plt.xlabel("Marketing Spend")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("marketing_vs_revenue.png")
plt.show()

# 6. Correlation Heatmap

plt.figure(figsize=(7, 5))
sns.heatmap(
    df[["Revenue", "Orders", "Marketing_Spend"]].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Sales Metrics Correlation")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# 7. Calculate business metrics

print("\n--- BUSINESS INSIGHTS ---")

print("Total Revenue:", df["Revenue"].sum())

print("Average Monthly Revenue:",
      round(df["Revenue"].mean(), 2))

print("Highest Revenue Month:",
      df.loc[df["Revenue"].idxmax(), "Month"])

print("Total Orders:", df["Orders"].sum())

print("Average Orders:",
      round(df["Orders"].mean(), 2))

print("\nVisualization completed successfully!")
