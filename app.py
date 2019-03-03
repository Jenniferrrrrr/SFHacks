import os
from flask import Flask, render_template, g, request
import requests
import random
import ipinfo
import Scraper
import json
from flask_bootstrap import Bootstrap

with open('config.json') as f:
    api_keys = json.load(f)

app = Flask(__name__)
bootstrap = Bootstrap(app)

local_resources = {}

@app.route('/')
def home():
    global local_resources
    zipcode = getZipCode()
    local_resources = Scraper.scraper(zipcode)
    names = local_resources.keys() 

    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
 
@app.route('/fw19')
def fw19():
    return render_template("fw19.html")

@app.route('/fw18')
def fw18():
    return render_template("fw18.html")

@app.route('/ss19')
def ss19():
    return render_template("ss19.html")

def getZipCode():
    ip_access_token = api_keys["ip_key"]
    handler = ipinfo.getHandler(ip_access_token)
    details = handler.getDetails()
    zipcode = details.postal
    return zipcode


if __name__ == '__main__':
    app.run(debug=True)
