/* Write your T-SQL query statement below */
(
    SELECT name as results  
    FROM (
        SELECT TOP 1 name, COUNT(*) AS cnt
        FROM MovieRating m
        LEFT JOIN Users u ON m.user_id = u.user_id
        GROUP BY name
        HAVING COUNT(*) = (
            SELECT MAX(rating_count)
            FROM (
                SELECT user_id, COUNT(*) AS rating_count
                FROM MovieRating
                GROUP BY user_id      
            ) AS subquery
        )
        ORDER BY cnt DESC, name ASC
    ) t
)
UNION ALL
(
    SELECT title AS name
    FROM (
        SELECT TOP 1 title, ROUND(SUM(rating) * 1.0 / COUNT(*), 2) AS res
        FROM MovieRating m
        LEFT JOIN Movies t ON t.movie_id = m.movie_id
        WHERE FORMAT(created_at, 'yyyy-MM') = '2020-02'
        GROUP BY title
        ORDER BY res DESC, title ASC
    ) u
)
ORDER BY name ASC;
