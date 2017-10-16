from twilio.rest import Client

#authentication
def send(msg):
    account_sid="AC12a2dc75eec3d322ff19e18088b06d26"
    auth_token="031659c7ed42adbe34164d4dfacbbe3c"
    client=Client(account_sid, auth_token)
    if msg:
        client.messages.create(
        to="+16476094668", 
        from_="+16479313347",
        body=msg)
    else:
        client.messages.create(
        to="+16476094668", 
        from_="+16479313347",
        body="Please come to my room.")
        
    
