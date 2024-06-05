import json
from flask import Blueprint, redirect, render_template, request, url_for, session
import requests
from web.repositories import *
from requests.auth import HTTPBasicAuth

ui_blueprint = Blueprint('ui', __name__) 


@ui_blueprint.route('/')
def home():
    return render_template("home.html")