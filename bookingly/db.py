import os
import psycopg2

try:
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    print(DATABASE_URL)

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
