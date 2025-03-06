/* Write your T-SQL query statement below */
-- select round(count(case when datediff(day,a.event_date,b.event_date)=1 then 1 end )*1.0/
-- count(distinct a.player_id),2) as fraction    from Activity a 
-- left join Activity b on a.player_id =b.player_id and a.event_date <b.event_date 
 
 select round(count(case when datediff(day,b.mm_date,a.event_date)=1 then 1 end )*1.0/
count(distinct a.player_id),2) as fraction  from Activity a left join 
 (select player_id ,min(event_date) as mm_date from Activity 
 group by player_id) b on a.player_id=b.player_id
 --where  datediff(day,b.mm_date,a.event_date)=1