/* Write your T-SQL query statement below */
select sell_date  ,count( product ) as num_sold ,STRING_AGG (product,',') within group
(order by product asc) as products       
from (select distinct * from Activities) a
group by sell_date