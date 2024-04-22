
USE Trabel;
GO
IF NOT EXISTS (SELECT * FROM sys.partition_functions WHERE name = 'PartitionFunction_RegisteredAt')
        BEGIN
            CREATE PARTITION FUNCTION PartitionFunction_RegisteredAt(INT)
            AS RANGE LEFT FOR VALUES ({values_clause});
            CREATE PARTITION SCHEME PartitionScheme_RegisteredAt
            AS PARTITION PartitionFunction_RegisteredAt
            ALL TO ([PRIMARY]);
        END

        IF NOT EXISTS (SELECT * FROM sys.indexes WHERE name = 'IX_{table_name}_{index_column}'
                                                                AND object_id = OBJECT_ID('{table_name}'))
        BEGIN
            CREATE CLUSTERED INDEX IX_{table_name}_{index_column} ON {table_name}({index_column})
            ON PartitionScheme_RegisteredAt({index_column});
            PRINT 'Clustered index and partition scheme created.'
        END
        ELSE
        BEGIN
            PRINT 'Clustered index already exists.'
        END
