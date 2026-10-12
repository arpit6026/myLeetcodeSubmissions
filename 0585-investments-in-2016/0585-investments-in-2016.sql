# Write your MySQL query statement below
select round(sum(t.tiv_2016), 2) as tiv_2016
from Insurance t
where (
    select count(t1.tiv_2015)
    from Insurance t1
    where t1.tiv_2015 = t.tiv_2015
) >= 2
AND
(
    SELECT count(*)
    from Insurance t2
    where t2.lat = t.lat and t2.lon = t.lon
) = 1