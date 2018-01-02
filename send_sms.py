from twilio.rest import Client

client = Client('ACf049ee52c4d5e94c3885a1c008d7d93f', 'fa792d0f44bc0a60bd93a88f78a195ce')

def sendSMS(message, num='(325) 864-2719'):
    client.messages.create(
        from_='(325) 400-2855',
        to=num,
        body=message,
        )