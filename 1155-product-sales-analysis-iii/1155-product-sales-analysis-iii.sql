/* Write your T-SQL query statement below */
select s.product_id ,(s.year) as first_year,
quantity ,
price 
  from  Sales s
inner join (
    select product_id ,min(year) as yr from Sales group by product_id
) t 
on s.product_id=t.product_id and s.year=t.yr
