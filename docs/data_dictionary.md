# Gold-layer data dictionary

The Gold layer is the business-ready star schema used by the SQL analytics layer. `fact_sales` is at order-line grain; the two dimensions provide descriptive context.

## `gold.dim_customers`

| Column | Meaning |
|---|---|
| `customer_key` | Surrogate key generated for the Gold customer dimension. |
| `customer_id` | CRM customer ID. |
| `customer_number` | CRM customer business key. |
| `first_name` | Customer first name. |
| `last_name` | Customer last name. |
| `country` | Standardised country from ERP location data. |
| `marital_status` | Standardised customer marital-status label. |
| `gender` | Customer gender; CRM is the master source and ERP fills `n/a` values. |
| `birthdate` | Customer birth date from ERP. |
| `create_date` | Customer creation date from CRM. |

## `gold.dim_products`

| Column | Meaning |
|---|---|
| `product_key` | Surrogate key generated for the Gold product dimension. |
| `product_id` | CRM product ID. |
| `product_number` | Cleaned product business key used to join sales. |
| `product_name` | Product name. |
| `category_id` | Product category identifier. |
| `category` | Product category from ERP product hierarchy. |
| `subcategory` | Product subcategory from ERP product hierarchy. |
| `maintenance` | Maintenance classification from ERP product hierarchy. |
| `cost` | Product cost. |
| `product_line` | Standardised product-line label. |
| `start_date` | Start date of the current product version. |

## `gold.fact_sales`

| Column | Meaning |
|---|---|
| `order_number` | Sales order number. |
| `product_key` | Foreign key to `gold.dim_products`. |
| `customer_key` | Foreign key to `gold.dim_customers`. |
| `order_date` | Sales order date. |
| `shipping_date` | Shipment date. |
| `due_date` | Due date. |
| `sales_amount` | Sales value for the order line. |
| `quantity` | Units sold on the order line. |
| `price` | Unit price used by the Silver transformation. |

## Downstream report views

| View | Purpose |
|---|---|
| `gold.report_customers` | One row per customer with age, segment, recency, order, revenue and purchase-behaviour metrics. |
| `gold.report_products` | One row per product with category, segment, sales, order, customer, pricing and recency metrics. |
