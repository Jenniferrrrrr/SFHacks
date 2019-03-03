import Scraper
import json
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from urllib.parse import urlencode

with open('twil.json') as f:
    api_keys = json.load(f)

onlineDictionary = {
                    "National Domestic Violence Hotline" : "www.thehotline.org", 
                    "The One Love Foundation" : "www.joinonelove.org", 
                    "The Anti Violence Project" : "www.avp.org"
                    }
                    
hotlineDictionary = {
                    "national domestic violence hotline" : "1 800 799 7233", 
                    "national child abuse hotline" : "1 800 422 4453",
                    "trans lifeline" : "1 877 565 8860"
                    }

def resources(dic):
    m = ""
    for item in dic:
        m = m + item + " at " + dic[item] + " , "
    return m

def localCall(zipcode, phone_number):
    """
    Scrapes for local domestic shelters and calls the user with top 3 results.
    """
    dictionary = Scraper.scraper(zipcode) 
    client = Client(api_keys["id"], api_keys["key"])
    message = "Here are local resources that you can find help from: " + resources(dictionary)
    client.calls.create(to=phone_number,from_='+16107569992', url="https://twimlets.com/message?" + urlencode({'Message': message}))

def hotlineCall(phone_number):
    """
    Calls the user with the name and number of 3 domestic abuse hotlines.
    """
    client = Client(api_keys["id"], api_keys["key"])
    message = "Here are hotlines that you can find help from: " + resources(hotlineDictionary)
    client.calls.create(to=phone_number,from_='+16107569992', url="https://twimlets.com/message?" + urlencode({'Message': message}))

def onlineCall(phone_number):
    """
    Calls the user with the name of three online resources and tips for accessing them discreetly.
    """
    client = Client(api_keys["id"], api_keys["key"])
    message = "Here are online resources that you can find help from: " + resources(onlineDictionary)
    client.calls.create(to=phone_number, from_='+16107569992', url="https://twimlets.com/message?" + urlencode({'Message': message}))