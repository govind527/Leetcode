/* Write your T-SQL query statement below */

select id,
case 
when p_id is null then 'Root'
when id in (select distinct t.p_id from Tree t) then 'Inner'
else 'Leaf'
end as type
from Tree;
