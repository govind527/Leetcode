select product_id, 10 as price
from Products
group by product_id
having min(change_date) > '2019-08-16'
union all 
select p.product_id,new_price from Products p 
join (
select product_id ,max(change_date) as change_date from Products 
where change_date<='2019-08-16'
group by product_id)q on p.product_id =q.product_id  and p.change_date=q.change_date