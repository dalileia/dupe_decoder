import pymysql.cursors
from flask import Flask


def db_connection():

  app = Flask(__name__)
  app.config.from_object('config.PyHelperConfig')
    
  mydb = pymysql.connect(
      host=app.config["ENV_MYSQL_HOST"],
      user=app.config["ENV_MYSQL_USER"],
      password=app.config["ENV_MYSQL_PASSWORD"],
      database="product",
      cursorclass=pymysql.cursors.DictCursor
    )
  
  return mydb



