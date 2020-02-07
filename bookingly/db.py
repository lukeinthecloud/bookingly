from configparser import ConfigParser
from boto.s3.connection import S3Connection
import os
import psycopg2

DATABASE_URL = S3Connection(os.environ['DATABASE_URL'])

print(DATABASE_URL)

try:
    connection = psycopg2.connect(DATABASE_URL)

    cursor = connection.cursor()

    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
