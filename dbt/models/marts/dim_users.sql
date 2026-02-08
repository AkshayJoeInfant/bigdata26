{{ config(
    materialized='incremental',
    unique_key='user_id'
) }}

WITH source_data AS (
    SELECT * FROM {{ source('raw_layer', 'users_batch') }}
),

-- This logic ensures we only insert NEW or CHANGED records
final AS (
    SELECT
        user_id,
        name,
        email,
        address,
        updated_at AS valid_from,
        -- In a real SCD2, we manage valid_to and is_current
        LEAD(updated_at) OVER (PARTITION BY user_id ORDER BY updated_at) AS valid_to,
        CASE 
            WHEN LEAD(updated_at) OVER (PARTITION BY user_id ORDER BY updated_at) IS NULL THEN TRUE 
            ELSE FALSE 
        END AS is_current
    FROM source_data
)

SELECT * FROM final