with dates as (

    select distinct

        order_purchase_date as date_value

    from {{ ref('stg_orders') }}

),

final as (

    select

        row_number() over (
            order by date_value
        ) as date_key,

        date_value,

        year(date_value) as year,
        month(date_value) as month,
        day(date_value) as day,

        quarter(date_value) as quarter

    from dates

)

select *
from final