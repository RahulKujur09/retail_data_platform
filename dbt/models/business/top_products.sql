with cta as (
        select
            p.product_category_name,
            s.order_id,
            s.price,
            s.payment_value
        from {{ref('fact_sales')}} as s
        left join {{ref('dim_products')}} as p
        on s.product_key = p.product_key
        ),

        final as (
        select
            product_category_name,
            count(order_id) as total_sales,
            round(avg(price), 2) as average_price,
            round(sum(payment_value), 2) as total_revenue,
            round(avg(payment_value), 2) as average_revenue
        from cta
        group by product_category_name

        )

        select
            *
        from final
        order by total_sales desc