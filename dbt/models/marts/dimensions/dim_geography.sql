with geography as (
    select distinct
        geolocation_zip_code_prefix,
        geolocation_city,
        geolocation_state
    from {{ref('stg_geolocation')}}
),

final as (
    select
        row_number() over(
            order by 
                geolocation_zip_code_prefix,
                geolocation_city,
                geolocation_state
        ) as geography_key,
        geolocation_zip_code_prefix,
        geolocation_city,
        geolocation_state

    from geography
)

select
    *
from final