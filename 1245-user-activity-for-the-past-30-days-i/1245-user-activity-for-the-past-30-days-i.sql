/* Write your T-SQL query statement below */
SELECT activity_date as day, COUNT(DISTINCT user_id) as active_users
FROM Activity
WHERE datediff(day,activity_date,'2019-07-27')<30 
AND activity_date <= '2019-07-27' 
GROUP BY activity_date