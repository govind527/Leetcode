/* Write your T-SQL query statement below */
--the question is simply asking to sum all inverstments in 2016 for all unique 
--locations for people with same investment in 2015 (obvoiusly more than one)..
--locations must be unique globally ,, not for same tiv 2015
select round(sum(tiv_2016),2) as tiv_2016   from Insurance i 
join (select lat,lon,count(*) as cnt from Insurance 
group by lat,lon
having count(*)=1) h on h.lat=i.lat and h.lon=i.lon
join 
(select tiv_2015  ,count(*) as ct  from Insurance 
group by tiv_2015
having count(*)>1) g on g.tiv_2015=i.tiv_2015