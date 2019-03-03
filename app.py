import os
from flask import Flask, render_template, g, request
import requests
import random
import ipinfo
import autocall
import json
from flask_bootstrap import Bootstrap

with open('config.json') as f:
    api_keys = json.load(f)

app = Flask(__name__)
bootstrap = Bootstrap(app)

phone_number = ""
zipcode = ""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
 
#online
@app.route('/fw19', methods=["GET", "POST"])
def fw19():
    global phone_number
    if request.method == 'POST':
        response = request.form
        phone_number = response["phone_number"]
        autocall.onlineCall(phone_number)
    return render_template("fw19.html")

#near me
@app.route('/fw18')
def fw18():
    global phone_number
    global zipcode
    if request.method == 'POST':
        response = request.form
        phone_number = response["phone_number"]
        zipcode = getZipCode()
        autocall.localCall(zipcode, phone_number)
    return render_template("fw18.html")

#hotlines
@app.route('/ss19')
def ss19():
    global phone_number
    if request.method == 'POST':
        response = request.form
        phone_number = response["phone_number"]
        autocall.hotlineCall(phone_number)
    return render_template("ss19.html")

def getZipCode():
    ip_access_token = api_keys["ip_key"]
    handler = ipinfo.getHandler(ip_access_token)
    details = handler.getDetails()
    zipcode = details.postal
    return zipcode


if __name__ == '__main__':
    app.run(debug=True)
