from configparser import ConfigParser

config = ConfigParser()

config['db'] = {
    'db_user': '',
    'db_password': '',
    'db_host': '',
    'db_port': '',
    'db_database': ''
}

with open('./dev.ini', 'w') as f:
    config.write(f)
