/* Write your T-SQL query statement below */
with cteq1 as (select distinct product_id  from 
Sales  where sale_date  between '2019-01-01' and '2019-03-31')
,ctenotq1 as (select distinct product_id  from 
Sales  where sale_date not  between '2019-01-01' and '2019-03-31')

select p.product_id,product_name  from cteq1 c
join Product p
on p.product_id=c.product_id
where p.product_id not in (select product_id from ctenotq1) 