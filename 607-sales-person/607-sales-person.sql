/* Write your T-SQL query statement below */
--name output

select s.name
from SalesPerson s
where sales_id not in (select sales_id from Orders
                      where com_id in (select com_id from Company where name='RED'))