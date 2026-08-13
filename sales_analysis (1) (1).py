"""
sales_analysis.py
Task: Sales Data Analysis with Pandas (CodeOrbit Tech - Data Analyst Internship)

Analyzes the cleaned sales dataset: calculates key metrics (total sales,
average order value, top products), groups/summarizes by region and by
month, and writes a short findings report.
"""
import pandas as pd

pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

# ---------------------------------------------------------------------------
# 1. Load cleaned data
# ---------------------------------------------------------------------------
df = pd.read_csv("cleaned_sales_data.csv", parse_dates=["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

report_lines = []


def add(line=""):
    print(line)
    report_lines.append(line)


add("# Sales Data Analysis — Findings Report\n")
add(f"Dataset: {len(df)} orders, {df['Order Date'].min().date()} to {df['Order Date'].max().date()}\n")

# ---------------------------------------------------------------------------
# 2. Key overall metrics
# ---------------------------------------------------------------------------
total_sales = df["Total Sales"].sum()
avg_order_value = df["Total Sales"].mean()
total_orders = len(df)
total_units = df["Quantity"].sum()

add("## Key Metrics")
add(f"- **Total Sales:** ${total_sales:,.2f}")
add(f"- **Total Orders:** {total_orders}")
add(f"- **Total Units Sold:** {total_units}")
add(f"- **Average Order Value:** ${avg_order_value:,.2f}")
add("")

# ---------------------------------------------------------------------------
# 3. Top products
# ---------------------------------------------------------------------------
top_products = (
    df.groupby("Product")["Total Sales"]
    .sum()
    .sort_values(ascending=False)
)
add("## Top Products by Sales")
for product, sales in top_products.items():
    add(f"- {product}: ${sales:,.2f}")
add("")

# ---------------------------------------------------------------------------
# 4. Sales by region
# ---------------------------------------------------------------------------
by_region = (
    df.groupby("Region")["Total Sales"]
    .agg(["sum", "mean", "count"])
    .rename(columns={"sum": "Total Sales", "mean": "Avg Order Value", "count": "Orders"})
    .sort_values("Total Sales", ascending=False)
)
add("## Sales by Region")
for region, row in by_region.iterrows():
    add(f"- {region}: ${row['Total Sales']:,.2f} total | "
        f"${row['Avg Order Value']:,.2f} avg order | {int(row['Orders'])} orders")
add("")

# ---------------------------------------------------------------------------
# 5. Sales by month (time period)
# ---------------------------------------------------------------------------
by_month = df.groupby("Month")["Total Sales"].sum().sort_index()
add("## Sales by Month")
for month, sales in by_month.items():
    add(f"- {month}: ${sales:,.2f}")
add("")

# ---------------------------------------------------------------------------
# 6. Top customers (bonus insight)
# ---------------------------------------------------------------------------
top_customers = (
    df.groupby("Customer")["Total Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)
add("## Top 5 Customers by Sales")
for customer, sales in top_customers.items():
    add(f"- {customer}: ${sales:,.2f}")
add("")

# ---------------------------------------------------------------------------
# 7. Summary of findings
# ---------------------------------------------------------------------------
best_product = top_products.index[0]
best_region = by_region.index[0]
best_month = by_month.idxmax()

add("## Summary")
add(
    f"Across {total_orders} orders totaling ${total_sales:,.2f} in sales, "
    f"**{best_product}** was the top-performing product, **{best_region}** was "
    f"the strongest region by revenue, and **{best_month}** was the "
    f"highest-selling month. The average order value across the dataset was "
    f"${avg_order_value:,.2f}."
)

# ---------------------------------------------------------------------------
# 8. Save outputs
# ---------------------------------------------------------------------------
with open("sales_analysis_report.md", "w") as f:
    f.write("\n".join(report_lines))

by_region.to_csv("summary_by_region.csv")
by_month.to_csv("summary_by_month.csv")
top_products.to_csv("summary_top_products.csv")

print("\nSaved: sales_analysis_report.md, summary_by_region.csv, summary_by_month.csv, summary_top_products.csv")
