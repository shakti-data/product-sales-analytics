# 03 · Python Analysis

Nine notebooks read the Gold and report views from SQL Server and turn them into analysis-ready tables, statistical findings, charts and business recommendations.

## Notebooks

| # | Notebook | Question | Main output |
|---|---|---|---|
| 01 | `01_data_quality_report.ipynb` | Is the data clean and consistent? | Cleaning checks and analysis-ready CSVs |
| 02 | `02_rfm_segmentation.ipynb` | Which customers matter most? | RFM segments and revenue concentration |
| 03 | `03_cohort_retention.ipynb` | Do customers come back? | Cohort retention matrix and heatmap |
| 04 | `04_product_profitability.ipynb` | Which products earn the most? | Product profitability and Pareto analysis |
| 05 | `05_churn_proxy_and_correlation.ipynb` | Who is inactive? | 90-day inactivity proxy and behaviour comparison |
| 06 | `06_statistics_and_hypothesis_testing.ipynb` | Are segment differences statistically meaningful? | Descriptive statistics, CI, correlation and hypothesis tests |
| 07 | `07_mom_trend_analysis.ipynb` | How do monthly sales move? | MoM growth and rolling averages |
| 08 | `08_executive_business_summary.ipynb` | What should an executive see first? | KPI, segment and product snapshots |
| 09 | `09_sales_forecast_baseline.ipynb` | What is a transparent baseline forecast? | Three-month moving-average forecast benchmark |

## Setup

1. Install ODBC Driver 17 for SQL Server and make sure the warehouse plus report views exist.
2. Install the Python packages:

```bash
pip install -r requirements.txt
```

3. Update [`config.py`](config.py) for your local SQL Server instance.
4. Run notebooks in order.

## Outputs

All notebook outputs are stored in [`output/`](output), including cleaned CSVs, summary tables, charts, the churn proxy outputs and the forecast files:

- `sales_baseline_forecast.csv`
- `sales_forecast_method_notes.csv`
- `15_sales_baseline_forecast.png`

## Method notes

- Python churn analysis uses the last order date in the dataset as its analysis date and defines inactivity as more than 90 days. It is a proxy, not a trained label.
- Notebook 09 excludes a partial latest month before calculating its three-month forecast baseline.
- The SQL report views (`gold.report_customers`, `gold.report_products`) must exist before running the notebooks.
