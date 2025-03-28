/* Write your T-SQL query statement below */
select employee_id , department_id
from Employee 
where primary_flag ='N' and employee_id not in (select employee_id from Employee
where primary_flag ='Y' )
group by employee_id,department_id
having count(*)=1
union 
select employee_id , department_id
from Employee 
where primary_flag ='Y'
