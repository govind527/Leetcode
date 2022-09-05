/* Write your T-SQL query statement below */
select request_at as Day,
round(avg(case when status = 'completed' then 0.0 else 1.0 END), 2) as [Cancellation Rate]
From Trips
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
AND client_id not in (select users_id from Users where banned='Yes')
AND driver_id not in (select users_id from Users where banned='Yes')
Group by request_at;
