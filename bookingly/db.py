import psycopg2
import configparser

config = configparser.ConfigParser()
config.read('../config-development.ini')

try:
    connection = psycopg2.connect(user=config['db']['db_user'],
                                  password=config['db']['db_password'],
                                  host=config['db']['db_host'],
                                  port=config['db']['db_port'],
                                  database=config['db']['db_database'])

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
