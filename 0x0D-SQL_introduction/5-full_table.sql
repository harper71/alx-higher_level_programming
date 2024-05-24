-- shows the discription of full table
SELECT CONCAT(
    'CREATE TABLE `', t.TABLE_NAME, '` (\n',
    c.columns,
    '\n) ENGINE=', t.ENGINE, 
    ' DEFAULT CHARSET=', SUBSTRING_INDEX(t.TABLE_COLLATION, '_', 1), 
    ' COLLATE=', t.TABLE_COLLATION, ';'
) AS create_statement
FROM information_schema.TABLES t
JOIN (
    SELECT 
        TABLE_SCHEMA,
        TABLE_NAME,
        GROUP_CONCAT(
            '  `', COLUMN_NAME, '` ', COLUMN_TYPE,
            IF(IS_NULLABLE = 'NO', ' NOT NULL', ''),
            IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT ', COLUMN_DEFAULT), ''),
            IF(EXTRA != '', CONCAT(' ', EXTRA), '')
            ORDER BY ORDINAL_POSITION
            SEPARATOR ',\n'
        ) AS columns
    FROM information_schema.COLUMNS
    WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = 'first_table'
    GROUP BY TABLE_SCHEMA, TABLE_NAME
) c ON t.TABLE_SCHEMA = c.TABLE_SCHEMA AND t.TABLE_NAME = c.TABLE_NAME
WHERE t.TABLE_SCHEMA = DATABASE() AND t.TABLE_NAME = 'first_table';
