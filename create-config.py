from configparser import ConfigParser

config = ConfigParser()

config['db'] = {
    'DATABASE_URL': ''
}

with open('./dev.ini', 'w') as f:
    config.write(f)
