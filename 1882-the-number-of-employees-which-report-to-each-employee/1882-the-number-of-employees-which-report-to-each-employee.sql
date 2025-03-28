/* Write your T-SQL query statement below */
select mgr.employee_id as employee_id  , mgr.name,count(emp.reports_to) as reports_count ,round(avg(emp.age*1.00),0) as  average_age 
  from  
Employees emp 
inner join Employees mgr
on emp.reports_to =mgr.employee_id 
group by mgr.employee_id , mgr.name
order by mgr.employee_id