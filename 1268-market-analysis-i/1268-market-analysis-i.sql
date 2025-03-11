SELECT 
  u.user_id AS buyer_id, 
  join_date, 
 count (o.item_id) AS orders_in_2019 
FROM 
  Users u 
  LEFT JOIN (select buyer_id,item_id from  Orders  where YEAR(order_date)= '2019' 
   )o ON u.user_id = o.buyer_id 
  
GROUP BY 
  u.user_id ,join_date
ORDER BY 
  u.user_id