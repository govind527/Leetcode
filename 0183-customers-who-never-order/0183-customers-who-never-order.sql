/* Write your T-SQL query statement below */
select name as Customers  from Customers  c
 where id not in (select customerId  from Orders  )