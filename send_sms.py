from twilio.rest import Client
import confidential

client = Client(confidential.twilio_client_arg1, confidential.twilio_client_arg2)

def sendSMS(message, num=confidential.phone_num):
    client.messages.create(
        from_=confidential.twilio_num,
        to=num,
        body=message,
        )