# Superstore Sales Analysis

## Project Overview

This project analyzes Superstore sales data to evaluate business performance across regions, product categories, and time periods. The analysis focuses on identifying sales trends, top-performing products, regional performance, and seasonal patterns that can support data-driven business decisions.

## Dataset

Source: Kaggle – Superstore Sales Dataset

The dataset contains information about:

* Orders
* Customers
* Products
* Regions
* Sales Transactions

### Key Columns

* Order_ID
* Order_Date
* Customer_ID
* Customer_Name
* Region
* Category
* Sub_Category
* Product_Name
* Sales

## Objectives

* Clean and prepare the sales dataset.
* Calculate key business KPIs.
* Analyze sales trends over time.
* Identify top and bottom-performing products.
* Compare sales performance across regions.
* Examine category-wise sales contribution.
* Perform seasonality analysis.
* Provide actionable business recommendations.

## Data Cleaning

The following preprocessing steps were performed:

* Removed duplicate records.
* Handled missing values.
* Standardized column names.
* Converted Order_Date to datetime format.
* Created Month and Year features for trend analysis.

## Key Performance Indicators (KPIs)

The following KPIs were calculated:

* Total Revenue
* Total Orders
* Average Order Value (AOV)

Note: The dataset did not contain a Profit column. Therefore, profit-based metrics could not be calculated using actual values.

## Visualizations

### Monthly Sales Trend

Displays sales performance over time to identify growth patterns and fluctuations.

### Regional Sales Analysis

Compares total sales across different regions.

### Category Analysis

Shows the contribution of each product category to overall sales.

### Top 10 Products

Highlights the highest revenue-generating products.

### Bottom 10 Products

Identifies products with the lowest sales performance.

### Seasonality Analysis

Evaluates monthly sales patterns to identify peak and low-demand periods.

## Key Findings

* Certain products consistently generated higher sales than others.
* Regional sales performance varied significantly.
* A few categories contributed a major share of total revenue.
* Sales exhibited seasonal trends with noticeable monthly fluctuations.
* Product-level analysis revealed opportunities for inventory optimization.

## Business Recommendations

1. Increase inventory levels for top-selling products.
2. Introduce promotional campaigns in low-performing regions.
3. Focus marketing efforts on high-revenue categories.
4. Optimize product assortment by reviewing low-selling products.
5. Launch targeted campaigns during peak seasonal periods.

## Technologies Used

* Python
* Pandas
* Plotly
* NumPy

## Project Structure

* Data Loading
* Data Cleaning
* KPI Calculation
* Exploratory Data Analysis
* Visualization
* Business Recommendations

## Conclusion

This analysis provides valuable insights into sales performance, customer demand patterns, and regional trends. The findings can help management improve decision-making, optimize inventory planning, and develop effective sales strategies.
