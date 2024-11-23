from twilio.rest import Client

account_sid = 'AC2644069da97b520138a8b9f0bbc15445'
auth_token = 'b2bf986a5eda3bebad5b920060b26bdb'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:[Phone Number]',
  body='[Content]',
  to='whatsapp:[Phone Number]'
)

print(message.sid)
print('Message Sent')