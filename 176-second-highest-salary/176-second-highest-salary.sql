/* Write your T-SQL query statement below */

with ctee as( select salary,dense_rank() over(order by salary desc) as rnum from Employee)
select isnull((select top 1 salary from ctee where rnum = 2),null) as SecondHighestSalary;