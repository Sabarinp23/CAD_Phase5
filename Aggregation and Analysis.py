Perform aggregate functions for analysis
SELECT Year, SUM(Sales) AS TotalSales
FROM SalesData
GROUP BY Year;