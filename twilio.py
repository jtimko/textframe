from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='' + os.environ['TWILIO_FROM'],
    body='Hello there!',
    to='' + os.environ['TWILIO_TO']
)

print(message.sid)