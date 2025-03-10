/* Write your T-SQL query statement below */
select d.name      as "Department"                     
        ,e1.name as "Employee"
        , e1.Salary as "Salary" from Employee e1
left join Employee e2 on e1.departmentId =e2.departmentId  and e1.salary <=e2.salary 
left join department d on d.id=e1.departmentId
group by d.name,e1.name,e1.Salary
having count(distinct e2.Salary)<=3