
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv(
"/kaggle/input/datasets/bhanupratapbiswas/superstore-sales/superstore_final_dataset (1).csv",
encoding="latin1"
)

# Clean columns
df.columns = df.columns.str.strip()

# Dates
df["Order_Date"] = pd.to_datetime(
df["Order_Date"],
errors="coerce"
)

# Create Profit (estimated)
df["Profit"] = df["Sales"] * 0.20

# Month-Year
df["Month"] = df["Order_Date"].dt.month_name()
df["Year"] = df["Order_Date"].dt.year

# -------------------
# KPIs
# -------------------

revenue = df["Sales"].sum()
profit = df["Profit"].sum()
orders = df["Order_ID"].nunique()

aov = revenue / orders

margin = (profit / revenue) * 100

print("Revenue:", revenue)
print("Profit:", profit)
print("Orders:", orders)
print("AOV:", round(aov, 2))
print("Profit Margin:", round(margin, 2), "%")

# -------------------
# Sales Trend
# -------------------

monthly = (
df.groupby(
df["Order_Date"].dt.to_period("M")
)["Sales"]
.sum()
.reset_index()
)

monthly["Order_Date"] = monthly["Order_Date"].astype(str)

fig = px.line(
monthly,
x="Order_Date",
y="Sales",
title="Monthly Sales Trend"
)

fig.show()

# -------------------
# Region Analysis
# -------------------

region = (
df.groupby("Region")
["Sales"]
.sum()
.reset_index()
)

fig = px.bar(
region,
x="Region",
y="Sales",
title="Regional Sales"
)

fig.show()

# -------------------
# Category Analysis
# -------------------

cat = (
df.groupby("Category")
["Sales"]
.sum()
.reset_index()
)

fig = px.pie(
cat,
names="Category",
values="Sales",
title="Category Contribution"
)

fig.show()

# -------------------
# Top Products
# -------------------

top = (
df.groupby(
"Product_Name"
)["Sales"]
.sum()
.sort_values(
ascending=False
)
.head(10)
.reset_index()
)

fig = px.bar(
top,
x="Sales",
y="Product_Name",
orientation="h",
title="Top 10 Products"
)

fig.show()

# -------------------
# Bottom Products
# -------------------

bottom = (
df.groupby(
"Product_Name"
)["Sales"]
.sum()
.sort_values()
.head(10)
.reset_index()
)

fig = px.bar(
bottom,
x="Sales",
y="Product_Name",
orientation="h",
title="Bottom 10 Products"
)

fig.show()

# -------------------
# Seasonality
# -------------------

season = (
df.groupby("Month")
["Sales"]
.sum()
.reset_index()
)

fig = px.bar(
season,
x="Month",
y="Sales",
title="Seasonality Analysis"
)

fig.show()
