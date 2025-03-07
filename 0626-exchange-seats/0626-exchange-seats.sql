/* Write your T-SQL query statement below */
with cnt as (select count(id) as totcnt from Seat)
select 
case when id%2!=0 and id!=totcnt then id+1
 when id%2!=0 and id=totcnt then id
 else id-1 end as id,
 student 
 from Seat
 cross join cnt
 order by id asc