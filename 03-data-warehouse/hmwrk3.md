
# Question 1:
Question 1: What is count of records for the 2024 Yellow Taxi Data?

> SELECT COUNT(*) FROM `kk-zoomcamp-2025.ny_taxi.external_yellow_trips`;
* 20,332,093

# Question 2:
Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

> SELECT COUNT(DISTINCT PULocationID) FROM `kk-zoomcamp-2025.ny_taxi.external_yellow_trips`; -- 155.12
> SELECT COUNT(DISTINCT PULocationID) FROM `kk-zoomcamp-2025.ny_taxi.yellow_trips`; -- 155.12
* 155.12 MB on both.
* could be cached results --> (0 MB for the External Table and 155.12 MB for the Materialized Table)

# Question 3:
Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table. Why are the estimated number of Bytes different?

> SELECT PULocationID FROM `kk-zoomcamp-2025.ny_taxi.yellow_trips`; -- 155.12
> SELECT PULocationID, DOLocationID FROM `kk-zoomcamp-2025.ny_taxi.yellow_trips`; -- 310.24

* BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

# Question 4:
How many records have a fare_amount of 0?

> SELECT COUNT(*) FROM `kk-zoomcamp-2025.ny_taxi.yellow_trips` WHERE fare_amount = 0; -- 8333
* 8,333

# Question 5:
What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)

* Partition by 'tpep_dropoff_datetime' and Cluster on 'VendorID'

# Question 6:
Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values?

> SELECT DISTINCT VendorID FROM `kk-zoomcamp-2025.ny_taxi.yellow_trips` WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15'; -- 310.24
> SELECT DISTINCT VendorID FROM `kk-zoomcamp-2025.ny_taxi.yellow_trips_prttnd` WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15'; -- 26.84
> SELECT DISTINCT VendorID FROM `kk-zoomcamp-2025.ny_taxi.yellow_trips_clstrd` WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15'; -- 310.24
> SELECT DISTINCT VendorID FROM `kk-zoomcamp-2025.ny_taxi.yellow_trips_prttnd1_clstrd2` WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15'; -- 310.24
> SELECT DISTINCT VendorID FROM `kk-zoomcamp-2025.ny_taxi.yellow_trips_prttnd_clstrd` WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15'; -- 26.84
* 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

# Question 7:
Where is the data stored in the External Table you created?

* GCP Bucket

# Question 8:
It is best practice in Big Query to always cluster your data:

* False

# Question 9:
No Points: Write a SELECT count(*) query FROM the materialized table you created. How many bytes does it estimate will be read? Why?

* estimate = 0B, actual = 0B; because BQ uses metadata to determine COUNT(*), instead of reading table data.