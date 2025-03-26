/* Write your T-SQL query statement below */
select project_id  ,round(sum(experience_years)*1.0/count(*),2) as average_years  from Project p
left join Employee e on p.employee_id =e.employee_id   
group by    project_id