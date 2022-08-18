/* Write your T-SQL query statement below */

select customer_number
from Orders
group by customer_number
having count(order_number)=(select max(num) from (select count(order_number) as num from 
                                                 Orders group by customer_number)t);