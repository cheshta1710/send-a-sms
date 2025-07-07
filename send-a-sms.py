import os
from twilio.rest import Client

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello! This is a test SMS from Python.",
    from_='+19*******',    #your twilio number   
    to='+91**********'     #receiver's phone number    
)

print("Message SID:", message.sid)
