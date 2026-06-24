# Data Quality Findings

## 1. Malformed Review Record

### Observation

One record in the `reviews` dataset contains:

* NULL review_id
* order_id populated with review text
* review_score = -1

### Investigation

The record appears to be malformed in the original source CSV due to incorrect quoting or delimiter parsing.

Example:

| Column       | Value                        |
| ------------ | ---------------------------- |
| review_id    | NULL                         |
| order_id     | material de boa qualidade... |
| review_score | -1                           |

### Resolution

The record is retained for lineage purposes.

The dbt `not_null(review_id)` test intentionally fails, highlighting a source system data quality issue rather than a transformation bug.

---

## 2. NULL Product and Seller Keys

### Observation

775 rows in `fact_sales` contain NULL values for:

* product_key
* seller_key

### Investigation

These rows correspond to:

* canceled orders
* unavailable orders

which never generated an associated order item.

Therefore:

```
orders
LEFT JOIN order_items
```

produces NULL product and seller references.

### Resolution

This behavior is expected and reflects valid business logic.

No data correction is required.
