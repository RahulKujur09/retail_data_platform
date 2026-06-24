with source as (

    select *
    from {{ source('silver', 'order_reviews') }}

),

final as (

    select

        review_id,
        order_id,
        review_score,
        review_comment_title,
        review_comment_message,

        review_creation_timestamp,
        review_answer_timestamp,

        review_creation_date,
        review_creation_time,

        review_answer_date,
        review_answer_time

    from source

)

select *
from final