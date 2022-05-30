# Write your MySQL query statement below
select e.name as Employee  from Employee e
join Employee f
on f.id=e.managerId
where f.salary<e.salary;


