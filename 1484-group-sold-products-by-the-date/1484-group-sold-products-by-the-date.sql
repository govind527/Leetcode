/* Write your T-SQL query statement below */
with ctte as (select distinct * from Activities) select sell_date,count(product) as num_sold,
string_agg(product, ',') within group (order by product) as products
from ctte 
group by sell_date
order by sell_date;

--//GROUP_CONCAT() function returns a string with concatenated non-NULL value from a group.
