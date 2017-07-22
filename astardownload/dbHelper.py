import configparser
cp = configparser.ConfigParser()
cp.read('myconfig.conf')
# cp.read('../../myconfig.conf')
db_name = cp.get('db', 'name')
db_user = cp.get('db', 'user')
db_password = cp.get('db', 'password')
db_host = cp.get('db', 'host')
db_port = cp.get('db', 'port')
