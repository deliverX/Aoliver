#!/usr/bin/python
import time
from twilio.rest import Client
import read_twilio_config as readConf

#text = 'aoliverJ'
 
auth_token = readConf.auth_token
account_sid = readConf.account_sid
from_ = readConf.from_

client = Client(account_sid,auth_token)
 
def sent_message(phone_number):
    mes = client.messages.create(
        from_='14076244898', 
        body=text,
        to=phone_number
    )
    print("OK")
 
 
#sent_message("+8618751996130")

