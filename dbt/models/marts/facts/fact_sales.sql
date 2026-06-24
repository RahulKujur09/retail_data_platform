{{
    config(

        materialized='incremental',

        unique_key=[
            'order_id',
            'order_item_id'
        ],

        incremental_strategy='delete+insert'

    )
}}

with orders as (

    select

        order_id,
        customer_id,
        order_status,
        order_purchase_date,
        order_purchase_timestamp

    from {{ ref('stg_orders') }}

    {% if is_incremental() %}

    where order_id not in (

        select distinct order_id

        from {{ this }}

                            )

    {% endif %}

),

order_items as (

    select

        order_id,
        order_item_id,
        product_id,
        seller_id,
        price,
        freight_value

    from {{ ref('stg_order_items') }}

),

payments as (

    select

        order_id,

        sum(payment_value) as payment_value

    from {{ ref('stg_payments') }}

    group by order_id

),

customers as (

    select

        customer_id,
        customer_key

    from {{ ref('dim_customers') }}

),

products as (

    select

        product_id,
        product_key

    from {{ ref('dim_products') }}

),

sellers as (

    select

        seller_id,
        seller_key

    from {{ ref('dim_sellers') }}

),

dates as (

    select

        date_value,
        date_key

    from {{ ref('dim_date') }}

),

final as (

    select

        o.order_id,

        c.customer_key,

        p.product_key,

        s.seller_key,

        d.date_key,

        oi.order_item_id,

        oi.price,

        oi.freight_value,

        pay.payment_value,

        o.order_status,

        current_timestamp as load_timestamp

    from orders o

    left join order_items oi

        on o.order_id = oi.order_id

    left join payments pay

        on o.order_id = pay.order_id

    left join customers c

        on o.customer_id = c.customer_id

    left join products p

        on oi.product_id = p.product_id

    left join sellers s

        on oi.seller_id = s.seller_id

    left join dates d

        on o.order_purchase_date = d.date_value

)

select *

from final