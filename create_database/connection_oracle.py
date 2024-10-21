import oracledb 
import os
from dotenv import load_dotenv

load_dotenv()
var_user     = os.getenv('USER')
var_password = os.getenv('PASSWORD')
var_dsn      = os.getenv('DSN')


def connection ():
  return oracledb.connect(user=var_user, password=var_password, dsn=var_dsn)