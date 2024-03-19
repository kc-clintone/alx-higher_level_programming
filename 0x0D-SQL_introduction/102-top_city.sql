-- Displays the top 3 of cities temp 
-- uring July & august ordered by temp (descending)

SELECT city, AVG(value)
AS avg_temp
FROM temperatures
WHERE month=7
OR month=8
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
