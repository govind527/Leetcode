/* Write your T-SQL query statement below */
select top 1 requester_id as id ,count(*) as num  from ( select requester_id from RequestAccepted 
union all
select accepter_id  from RequestAccepted) t 
group by t.requester_id 
order by num desc