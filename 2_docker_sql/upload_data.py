
import argparse

import os

import psycopg2

import pandas as pd
from time import time

import sqlalchemy

def main(params):

    """ Ingest Data Arguments """

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    dbname = params.dbname
    table = params.table
    source_url = params.source_url
    csv_name = 'output.csv'
        #"../yellow_tripdata_Jan2021/yellow_tripdata_2021-01.csv"

    os.system(f'wget {source_url} -O {csv_name}')


    """ Connect to DB """
    engine = sqlalchemy.create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
    engine.connect()


    """ Load Data into DB

    # create a DB using the column names of the pandas dataset     
    # print(pd.io.sql.get_schema(frame=sample_df, name=table, con=engine))

    # create an iterator to load the csv dataset into DB in manageable chunks

    1. access dataset column names and use them as db columns
    2. upload dataset in iterations, ensuring the datetime(TEXT) columns are updated to datetime(TIMESTAMP)

    Note: Do not call the iterator outside of uploading rows,
        whatever chunk is called is no longer available later when uploading.

    * we need to catch 'StopIteration' error when it finishes loading all rows -- RESOLVED
    * our iteration is starting at 100000 because 'dataset_iter' was called earlier in testing -- RESOLVED
    """

    dataset_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)

    pd.read_csv(csv_name, header=0, nrows=0
                            ).to_sql(name=table, con=engine, if_exists='replace')

    while True:
        try:
            # track time
            started = time()

            # this assignment overrides earlier assignment
            upload_df = next(dataset_iter)

            upload_df.tpep_pickup_datetime = pd.to_datetime(upload_df.tpep_pickup_datetime)
            upload_df.tpep_dropoff_datetime = pd.to_datetime(upload_df.tpep_dropoff_datetime)

            # now after the db has been set up, load rows in chunks, appending (not replacing)
            upload_df.to_sql(name=table, con=engine, if_exists='append')

            finished = time()

            print(f'inserted {len(upload_df)} rows in {(finished - started):.2f} seconds')

        except StopIteration:
            break

    print(f'inserting rows is complete')

    # """ Issues to Resolve
    # 1. the DB columns have the data type of the source csv     
    # 2. NULL values could be causing the error about mixed types      
    #     * 'C:\Users\kingo\AppData\Local\Temp\ipykernel_18380\608689963.py:24: 
    #     DtypeWarning: Columns (6) have mixed types. 
    #     Specify dtype option on import or set low_memory=False. 
    #     upload_df = next(dataset_iter)'
    # """
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Ingest CSV data into Postgres")

    parser.add_argument('--user', help="name of the user")
    parser.add_argument('--password', help="password of the user")
    parser.add_argument('--host', help="name of the host")
    parser.add_argument('--port', help="number of the access port")
    parser.add_argument('--dbname', help="name of the destination db")
    parser.add_argument('--table', help="name of the destination table")
    parser.add_argument('--source_url', help="url of the source file")

    args = parser.parse_args()

    main(args)