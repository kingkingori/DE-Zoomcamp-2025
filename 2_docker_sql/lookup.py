# import libraries

import pandas as pd
import psycopg2
import sqlalchemy

import argparse


def main(params):
    # define parameters

    user = params.user
    password = params.password
    host = params.host
    port = params.port
    dbname = params.dbname
    table_name = params.table_name
    # source_url = params.source_url
    source_url = "../taxi_zone_lookup.csv"

    # create engine

    engine = sqlalchemy.create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
    engine.connect()

    # create and load lookup table

    pd.read_csv(source_url, header=0, nrows=0).to_sql(name=table_name, con=engine, if_exists="replace")
    pd.read_csv(source_url, header=0).to_sql(name=table_name, con=engine, if_exists="append")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Create lookup table and load it")

    parser.add_argument('--user', help="name of the user")
    parser.add_argument('--password', help="password of the user")
    parser.add_argument('--host', help="name of the host")
    parser.add_argument('--port', help="number of the access port")
    parser.add_argument('--dbname', help="name of the destination db")
    parser.add_argument('--table_name', help="name of the destination table")
    parser.add_argument('--source_url', help="url of the source file")

    args = parser.parse_args()

    main(args)