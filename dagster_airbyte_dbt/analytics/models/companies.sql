{{ config(materialized = "table")}}

select
    _airbyte_data."Sales Rep Id" as sales_rep_id,
    _airbyte_data."Company Id" as company_id,
    _airbyte_data."Sales Rep" as sales_rep_name,
    _airbyte_data."Company Name" as company_name,
from 
    {{ source('airbyte', '_airbyte_raw_sales__companies') }} as _airbyte_data
    -- example.main._airbyte_raw_sales__companies