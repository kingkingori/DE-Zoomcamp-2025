# Question 1.
> docker run -it --entrypoint=bash python:3.12.8    
> root@3a561379c239:/# pip --version
* Answer: 24.3.1 

# Question 2.
> on compose.yaml, it is the service name or container_name, and the container port (second one)
* Answer: db:5432

# Question 3.
SELECT COUNT(*) FROM public.green_taxi WHERE trip_distance > 1 AND trip_distance <= 3
AND lpep_dropoff_datetime >= TIMESTAMP '2019-10-01' AND lpep_dropoff_datetime < TIMESTAMP '2019-11-01';
* Answer: 104802 ; 198924 ; 109603 ; 27678 ; 35189

# Question 4.
SELECT * FROM public.green_taxi WHERE trip_distance = (
    SELECT MAX(trip_distance) FROM public.green_taxi
);
* Answer: "2019-10-31 23:23:41"

# Question 5.
WITH loc_amounts AS (
    SELECT "PULocationID" AS location_id, SUM(total_amount) AS amount 
    FROM public.green_taxi WHERE lpep_pickup_datetime::DATE = '2019-10-18'
    GROUP BY 1 ORDER BY 2 DESC LIMIT 3
)
SELECT z."Zone", la.amount FROM loc_amounts la JOIN public.lookup_table z 
ON la.location_id = z."LocationID" ORDER BY 2 DESC;
* Answer: "East Harlem North", "East Harlem South", "Morningside Heights"

# Question 6.
WITH loc_tips AS (
    SELECT "DOLocationID", MAX(tip_amount) max_tip FROM public.green_taxi
    WHERE EXTRACT(YEAR FROM lpep_pickup_datetime) = '2019' AND EXTRACT(MONTH FROM lpep_pickup_datetime) = '10' 
    AND "PULocationID" = (SELECT "LocationID" FROM public.lookup_table WHERE "Zone" ILIKE 'East Harlem North')
    GROUP BY 1 ORDER BY 2 DESC LIMIT 1
	)
SELECT z."Zone" FROM public.lookup_table z JOIN loc_tips t ON z."LocationID" = t."DOLocationID";
* Answer: "JFK Airport"

# Question 7.
1. Downloading the provider plugins and setting up backend,
2. Generating proposed changes and auto-executing the plan,
3. Remove all resources managed by terraform.
* Answer: terraform init, terraform apply -auto-approve, terraform destroy