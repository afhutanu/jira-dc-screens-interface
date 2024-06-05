from flask import Flask, request, render_template_string, redirect, url_for, jsonify, session
from web.blueprints import ui, api

import requests
import psycopg2
import json

app = Flask(__name__, static_folder='web/static', template_folder='web/templates')
app.config['SECRET_KEY'] = '19250u12h0912b01bBGb2'


app.register_blueprint(ui.ui_blueprint)
app.register_blueprint(api.api_blueprint)


@app.before_request
def session_credentials():
    global loginType

    if 'username' in session and 'password' in session:
        global basicAuthUsername
        global basicAuthPassword
        
        basicAuthUsername = session['username']
        basicAuthPassword = session['password']
        loginType = 'basic'
        

    if 'token' in session:
        global bearerToken
        bearerToken = session['token']
        loginType = 'bearer'


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5001)