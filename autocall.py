import Scraper
import json
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from urllib.parse import urlencode

with open('twil.json') as f:
    api_keys = json.load(f)


def resources(dic):
    m = ""
    for item in dic:
        m = m + item + " at " + dic[item] + " , "
    return m

def call(ipadress):
    """
    Some example usage of different twilio resources.
    """
    dictionary = Scraper.scraper(ipadress) 
    client = Client(api_keys["id"], api_keys["key"])
    message = "Here are local resources that you can find help from: " + resources(dictionary)
    client.calls.create(to='+15109449663',from_='+16107569992', url="https://twimlets.com/message?" + urlencode({'Message': message}))

if __name__ == '__main__':
    call(ipadress)

