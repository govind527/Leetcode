/* Write your T-SQL query statement below */
select x,y,z,
case when 
x + y > z and 
x + z > y and 
y + z > x Then 'Yes' else 'No' end as triangle 
from  Triangle 