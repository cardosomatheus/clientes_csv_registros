import os
from dotenv import load_dotenv

load_dotenv()
var_user = os.getenv('USER')

print(var_user)