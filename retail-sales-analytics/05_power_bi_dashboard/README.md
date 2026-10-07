# 05 · Power BI Dashboard

`sales_dashboard.pbix` is the final visual layer for overall sales and product performance.

## Pages

| Page | Content |
|---|---|
| Sales Performance Dashboard | KPI cards, category slicer, yearly orders trend and sales by product |
| Product Summary | Top products by orders with sales, customers, average monthly sales, AOV and an orders-over-time sparkline |

![Sales performance dashboard](screenshots/page1.png)

![Product summary](screenshots/page2.png)

## Data

The model reads the cleaned CSV outputs produced by notebook 01:

- [`df_customers_clean_v2.csv`](../03_python_analysis/output/df_customers_clean_v2.csv)
- [`df_products_clean.csv`](../03_python_analysis/output/df_products_clean.csv)
- [`df_sales_clean_v2.csv`](../03_python_analysis/output/df_sales_clean_v2.csv)

If Power BI cannot find the files after download, use **Home → Transform data → Data source settings** and point the connections to `03_python_analysis/output`.
