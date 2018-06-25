import os
from flask import Flask, request
import requests
from dateutil import parser, tz
from twilio.twiml.messaging_response import MessagingResponse
 
app = Flask(__name__)
to_zone = tz.gettz('America/New_York')

@app.route('/', methods=['POST'])
def receive_sms():
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    resp.message(body or 'Hello World!')
    return str(resp)
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
