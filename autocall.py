import Scraper
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from urllib.parse import urlencode

ACCOUNT_SID = 'AC178a6cc50c2ab3a86e0bb881e4c2136a'
AUTH_TOKEN = '54b7c93db5df551f6f7bbfc2fedd21f5'
dictionary = Scraper.scraper("94720") #Dummy call
def resources(dic):
    m = ""
    for item in dic:
        m = m + item + " at " + dic[item] + " , "
    return m

def call():
    """
    Some example usage of different twilio resources.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = "Here are local resources that you can find help from: " + resources(dictionary)
    client.calls.create(to='+15109449663',from_='+16107569992', url="https://twimlets.com/message?" + urlencode({'Message': message}))

if __name__ == '__main__':
    call()

