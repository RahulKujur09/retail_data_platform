with sales as (
        select
            *
        from {{ref('fact_sales')}} as s
        left join {{ref('dim_date')}} as d
        on s.date_key = d.date_key
        ),
        final as (
        select
            date_value,
            count(distinct order_id) as total_order,
            round(sum(payment_value), 2) as total_sales,
            round(avg(payment_value), 2) as average_order_value,
            round(sum(freight_value), 2) as total_freight

        from sales
        group by date_value
        )

        select
            *
        from final
        order by date_value