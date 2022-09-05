/* Write your T-SQL query statement below */
select Department,Employee,Salary from (select  d.name as Department,e.name as Employee,e.salary as Salary,
dense_rank() over(partition by d.name order by e.salary desc) as rnum
from Employee e join
Department d on e.departmentId=d.id) tmp
where tmp.rnum=1;
