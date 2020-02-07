from configparser import ConfigParser
import os
import psycopg2

parser = ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), r"dev.ini"))
parser.read('dev.ini')

db_config = {
    'user': parser.get('db', 'db_user'),
    'password': parser.get('db', 'db_password'),
    'host': parser.get('db', 'db_host'),
    'port': parser.get('db', 'db_port'),
    'database': parser.get('db', 'db_database')
}

try:
    connection = psycopg2.connect(user=db_config['user'],
                                  password=db_config['password'],
                                  host=db_config['host'],
                                  port=db_config['port'],
                                  database=db_config['database'])

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
