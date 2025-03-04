/* Write your T-SQL query statement below */
select FORMAT(trans_date,'yyyy-MM') as month,country 
,count(*) as trans_count ,
count(case when state='approved' then 1 end) as approved_count,
sum(amount) as trans_total_amount,
sum(case when state='approved' then amount else 0 end) as approved_total_amount
  from Transactions 
group by FORMAT(trans_date,'yyyy-MM') ,country