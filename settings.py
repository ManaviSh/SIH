# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv
 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
 
# Accessing variables.
status = os.getenv('STATUS')
secret_key = os.getenv('SECRET_KEY')
 
# Using variables.
print(status)
print(secret_key)