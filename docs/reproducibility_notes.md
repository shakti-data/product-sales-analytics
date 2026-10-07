# Reproducibility note

The SQL report views `gold.report_customers` and `gold.report_products` use `GETDATE()` to calculate customer age and recency. These values therefore depend on the date the view is queried, and they will change if the view is run on a different day.

Current handling:

- The Python churn analysis uses the last order date in the dataset (`2014-01-28`) as its analysis date, so its results are stable between runs.
- The SQL report views still calculate age and recency against the query date. Replacing `GETDATE()` with a fixed date would change the meaning of age and recency and every number that depends on them, so the views were kept as they are and the behaviour is documented here.

A possible improvement is an `@analysis_reference_date` parameter, or versioned report views, so that the SQL results can be reproduced exactly.
