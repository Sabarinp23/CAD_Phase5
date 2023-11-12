Join multiple tables for more complex queries
SELECT W.ColumnA, T.ColumnX
FROM WarehouseTable W
INNER JOIN AnotherTable T ON W.ID = T.ID;