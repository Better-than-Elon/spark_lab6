### Run docker compose first
### Main file: cluster.py
```
$ poetry run python cluster.py 
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
24/06/29 14:28:08 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
2024-06-29 14:28:21,987 — data_processing — INFO — Input data
root
 |-- completeness: double (nullable = false)
 |-- energy_100g: double (nullable = false)
 |-- energy-kcal_100g: double (nullable = false)
 |-- carbohydrates_100g: double (nullable = false)
 |-- proteins_100g: double (nullable = false)
 |-- fat_100g: double (nullable = false)
 |-- sugars_100g: double (nullable = false)
 |-- saturated-fat_100g: double (nullable = false)
 |-- salt_100g: double (nullable = false)
 |-- sodium_100g: double (nullable = false)

24/06/29 14:28:22 WARN SparkStringUtils: Truncated the string representation of a plan since it was too large. This behavior can be adjusted by setting 'spark.sql.debug.maxToStringFields'.
24/06/29 14:28:23 WARN JdbcUtils: Requested isolation level 1 is not supported; falling back to default isolation level 2
24/06/29 14:28:23 WARN JdbcUtils: Requested isolation level 1 is not supported; falling back to default isolation level 2
24/06/29 14:28:23 WARN JdbcUtils: Requested isolation level 1 is not supported; falling back to default isolation level 2
24/06/29 14:28:23 WARN JdbcUtils: Requested isolation level 1 is not supported; falling back to default isolation level 2
24/06/29 14:28:23 WARN JdbcUtils: Requested isolation level 1 is not supported; falling back to default isolation level 2
24/06/29 14:28:23 WARN JdbcUtils: Requested isolation level 1 is not supported; falling back to default isolation level 2
24/06/29 14:28:23 WARN JdbcUtils: Requested isolation level 1 is not supported; falling back to default isolation level 2
2024-06-29 14:28:24,225 — __main__ — INFO — Dataset uploaded to db: `completeness` FLOAT, `energy_100g` FLOAT, `energy-kcal_100g` FLOAT, `carbohydrates_100g` FLOAT, `proteins_100g` FLOAT, `fat_100g` FLOAT, `sugars_100g` FL
OAT, `saturated-fat_100g` FLOAT, `salt_100g` FLOAT, `sodium_100g` FLOAT
2024-06-29 14:28:24,978 — data_processing — INFO — VectorAssembler
+----------------------------------------+
|                                features|
+----------------------------------------+
|                        (10,[0],[0.375])|
|                       (10,[0],[0.4625])|
|[0.2,448.0,107.0,3.5,7.5,6.8,1.6,1.8,...|
|[0.375,174.0,41.6666666667,5.0,3.3333...|
|(10,[0,1,2,3,6],[0.375,134.0,32.0,8.0...|
+----------------------------------------+
only showing top 5 rows

2024-06-29 14:28:27,268 — data_processing — INFO — StandardScaler
+----------------------------------------+
|                          scaledFeatures|
+----------------------------------------+
|            (10,[0],[2.213270362432414])|
|            (10,[0],[2.729700113666644])|
|[1.1804108599639542,0.108635164522463...|
|[2.213270362432414,0.0421931219350640...|
|(10,[0,1,2,3,6],[2.213270362432414,0....|
+----------------------------------------+
only showing top 5 rows

24/06/29 14:28:32 WARN InstanceBuilder: Failed to load implementation from:dev.ludovic.netlib.blas.JNIBLAS
2024-06-29 14:28:38,494 — data_processing — INFO — Silhouette Score for k = 12 is 0.4200739132705623
24/06/29 14:28:38 WARN JdbcUtils: Requested isolation level 1 is not supported; falling back to default isolation level 2
2024-06-29 14:28:39,669 — __main__ — INFO — Predictions saved
SUCCESS: The process with PID 7904 (child process of PID 17596) has been terminated.
SUCCESS: The process with PID 17596 (child process of PID 13920) has been terminated.
SUCCESS: The process with PID 13920 (child process of PID 12324) has been terminated.
```