# Archivo de configuración para la base de datos MySQL

config_db1 = {
  'user': 'data',
  'password': 'khQ9--mp6LWq97iA',
  'host': 'ec2-52-24-250-253.us-west-2.compute.amazonaws.com',
  'database': 'movielens',
}

config_db2 = {
  'user': 'sa',
  'password': 'khQ9--mp6LWq97iA',
  'host': 'localhost',
  'database': 'movielens',
}

url_db1 = "mysql+mysqlconnector://data:khQ9--mp6LWq97iA@ec2-52-24-250-253.us-west-2.compute.amazonaws.com:3306/movielens"

if __name__ == "__main__":
    print("""
    Config MySQL 1:
    ---------------------
    User: {user}
    Password: {password}
    Host: {host}
    Database: {database}
    ---------------------
    """.format(**config_db1))
