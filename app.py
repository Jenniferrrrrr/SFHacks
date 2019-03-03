import os
from flask import Flask, render_template, g, request
import requests
import random
import ipinfo
import Scraper
import json

with open('config.json') as f:
    api_keys = json.load(f)

app = Flask(__name__)

@app.route('/')
def home():
    zipcode = getZipCode()
    local_resources = Scraper.scraper(zipcode)
    render_template('index.html', local_resources = local_resources)

@app.route('/about')
def about():
    render_template('about')
 

def getZipCode():
    ip_access_token = api_keys["ip_key"]
    handler = ipinfo.getHandler(ip_access_token)
    details = handler.getDetails()
    zipcode = details.postal
    return zipcode


if __name__ == '__main__':
    app.run(debug=True)
