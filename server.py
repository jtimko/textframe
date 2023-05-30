from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request
import os
import requests

DOWNLOAD_DIRECTORY = os.getcwd() + '/img/'
app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms():
    resp = MessagingResponse()
    if request.values['NumMedia'] != 0:
        filename = request.values['MessageSid'] + '.jpg'
        with open("{}/{}".format(DOWNLOAD_DIRECTORY, filename), 'wb') as f:
            image_url = request.values['MediaUrl0']
            f.write(requests.get(image_url).content)

        resp.message("Thanks for the image!")
    else:
        resp.message("Try sending a picture message.")

    return str(resp)

def start_server():
    app.run()

if __name__ == '__main__':
    start_server()


