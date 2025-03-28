/* Write your T-SQL query statement below */
select contest_id ,round(count(*)*100.0/(select count(distinct user_id)from Users ),2)
 as percentage  from  Users u 
inner join  Register r on r.user_id=u.user_id
group by contest_id
order by percentage desc,contest_id  asc