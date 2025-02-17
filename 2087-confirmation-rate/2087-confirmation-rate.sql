/* Write your T-SQL query statement below */
select s.user_id,cast((sum(case when c.action ='confirmed' then 1 else 0 end)*1.0/count(*)) 
as numeric(10,2)) as confirmation_rate 
from Signups s
left join Confirmations  c on c.user_id=s.user_id
group by s.user_id

-- select user_id ,c.action,count(*)
-- -- from Signups s
-- from Confirmations c 
-- group by user_id ,c.action  
-- having c.action='confirmed'

-- select user_id ,sum(case when c.action ='confirmed' then 1 else 0 end)as total,count(*) as ttoal

-- -- from Signups s
-- from Confirmations c 
-- --where c.action ='confirmed'
-- group by user_id   
-- --having c.action='confirmed'