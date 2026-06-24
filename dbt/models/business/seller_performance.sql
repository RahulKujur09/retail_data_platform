with cte as (
            select
                fs.seller_key,
                ds.seller_city as city,
                ds.seller_state as state,
                fs.order_id as orders,
                fs.payment_value as total_revenue
            from {{ref('fact_sales')}} as fs
            left join {{ref('dim_sellers')}} as ds
            on fs.seller_key = ds.seller_key
            ),

            final as (
            select
                seller_key as seller,
                state,
                city,
                count(orders) as total_sales,
                round(sum(total_revenue), 2) as total_revenue,
                round(avg(total_revenue), 2) as average_revenue
            from cte
            group by seller_key, city, state
            order by total_revenue desc
            )

            select
                *
            from final