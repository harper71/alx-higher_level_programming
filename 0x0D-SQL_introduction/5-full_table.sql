-- shows the discription of full table
SELECT 
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM 
    information_schema.COLUMNS
WHERE 
    TABLE_NAME = 'first_table';