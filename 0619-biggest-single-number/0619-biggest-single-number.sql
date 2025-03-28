/* Write your T-SQL query statement below */
select coalesce(max(num),null) as num from (select num ,count(*) as cnt from MyNumbers 
group by num
having count(*)=1)t
