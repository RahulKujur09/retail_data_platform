with cte as(
        select
            fs.customer_key as customer,
            dc.customer_state as state,
            dc.customer_city as city,
            fs.order_id as orders,
            fs.payment_value as purchase,
            dp.product_category_name as product_category
        from {{ref('fact_sales')}} as fs
        left join {{ref('dim_customers')}} as dc
        on fs.customer_key = dc.customer_key
        left join {{ref('dim_products')}} as dp
        on fs.product_key = dp.product_key
        ),

        final as (
        select
            customer,
            state,
            city,
            product_category,
            count(orders) as items_orderd,
            round(sum(purchase), 2) as total_purchase
        from cte
        group by customer, state, city, product_category
        order by total_purchase desc
        )

        select
            *
        from final