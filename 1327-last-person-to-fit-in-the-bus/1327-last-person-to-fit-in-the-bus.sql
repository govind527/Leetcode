/* Write your T-SQL query statement below */
with cte as (select *,sum(Weight ) over(order by Turn,Weight ) as rnk from Queue 
),cte2 as (select * from cte 
where rnk <=1000
)
select person_name  from cte2
where turn =(select max(turn) from cte2)

 
