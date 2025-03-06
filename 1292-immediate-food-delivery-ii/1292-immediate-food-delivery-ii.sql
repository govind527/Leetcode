# Write your MySQL query statement below
/* Write your T-SQL query statement below */
select round(count(case when order_date = customer_pref_delivery_date then 1 end )*100.0/ 
count(*),2) as immediate_percentage 
from Delivery 
where (customer_id,order_date)  in (select customer_id,min(order_date )as ttt  from Delivery
group by customer_id )