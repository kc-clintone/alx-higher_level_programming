-- displays the average temp by city ordered by temp  ascending)

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
