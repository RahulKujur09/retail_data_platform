with source as (

    select *
    from {{ source('silver', 'order_items') }}

),

final as (

    select

        order_id,
        order_item_id,
        product_id,
        seller_id,
        shipping_limit_timestamp,
        price,
        freight_value

    from source

)

select *
from final