with products as (
    select
        *
    from {{ref('stg_products')}}
),

final as (
    select
        row_number() over(
            order by product_id
        ) as product_key,
        product_id,
        product_category_name,
        product_name_lenght,
        product_description_lenght,
        product_photos_qty,
        product_weight_g,
        product_length_cm,
        product_height_cm,
        product_width_cm
    from products
)

select
    *
from final