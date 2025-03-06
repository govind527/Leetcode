/* Write your T-SQL query statement below */

--with ctea  as (select num,min(id) as id from Logs group by num)
-- select distinct l.num as ConsecutiveNums  
-- from Logs l 
--  join Logs m on l.id=m.id+1 and l.num=m.num
--  join Logs n on l.id=n.id+2 and l.num=n.num
-- where (l.num-coalesce(m.num,l.num))=0
-- group by l.num
-- having count(8)>=3

WITH src as (SELECT CASE WHEN t.num = LEAD(t.num) OVER(ORDER BY id)
AND t.num = LEAD(t.num,2) OVER(ORDER BY id)
THEN t.num
END as ConsecutiveNums FROM Logs t )
SELECT DISTINCT src.ConsecutiveNums FROM src WHERE src.ConsecutiveNums IS NOT NULL