/* Write your T-SQL query statement below */
-- select u.name as [name], CASE 
-- WHEN u.id NOT IN (SELECT user_id FROM Rides) THEN 0
-- ELSE
-- 	SUM(r.distance) 
-- END AS [travelled_distance]
-- from Users u
-- left join Rides r on u.id=r.user_id
-- group by r.user_id
-- order by travelled_distance desc,name asc
With CTE as
(
    select u.id, u.Name, CASE 
    WHEN u.id NOT IN (SELECT user_id FROM Rides) THEN 0
    ELSE SUM(r.distance) END AS [travelled_distance]
    from Users u left join Rides r on r.user_id = u.id
    group by u.id, u.Name
)
select Name, travelled_distance from CTE order by travelled_distance desc, Name