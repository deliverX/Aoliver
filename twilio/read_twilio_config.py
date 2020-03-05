#!/usr/bin/python
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.append(BASE_DIR)
from common.read_config import ReadConfig

data = ReadConfig('twilio.config')
auth_token = data.get_db("twilio","auth_token")
account_sid = data.get_db("twilio","account_sid")
from_ = data.get_db("twilio","from_")

