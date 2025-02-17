/* Write your T-SQL query statement below */
select mgr.name--,emp.managerId,count(*) 
from Employee emp
 join Employee mgr
on emp.managerId =mgr.id
--where mgr.name is not null
group by mgr.name,emp.managerId
having count(distinct emp.id)>=5