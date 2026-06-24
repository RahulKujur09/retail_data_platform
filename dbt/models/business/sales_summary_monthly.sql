with sales as (
        select
            *
        from {{ref('fact_sales')}} as s
        left join {{ref('dim_date')}} as d
        on s.date_key = d.date_key
        ),
        final as (
        select
            year as sales_year,
            month as sales_month,
            count(distinct order_id) as total_order,
            round(sum(payment_value), 2) as total_sales,
            round(avg(payment_value), 2) as average_order_value,
            round(sum(freight_value), 2) as total_freight

        from sales
        group by sales_year, sales_month
        )

        select
            *
        from final
        order by sales_year, sales_month