import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC2d9b8d775c96813a62abded01b5c5120'
auth_token = '36962f21e324450d02699507007ceba3'

client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say voice="alice">Hello Surucha Arora, the aalsi cute bachi, get up and login, i am still waiting for my reward, just kidding dont worry. here is a song for my girl, love chit chiti </Say><Play>https://pyaaribaarish.000webhostapp.com/ilysa.mp3</Play></Response>',
                        to='+917988683350',
                        from_='+12564154635'
                    )
                    #
                                                                                                    
print(call.sid)
