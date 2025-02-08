/* Write your T-SQL query statement below */
select Emp.name  as Employee  
from 
Employee Emp 
 join Employee man on Emp.managerId=man.id and Emp.salary>man.salary