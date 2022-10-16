from urllib import response
from flask import Flask, redirect, url_for, request, render_template, session, make_response
import requests
import os
import uuid
import json
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)

    return response


@app.route("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")
    return render_template("index.html", user_ip=user_ip)


hostname = input("Enter the  hostname of the Router:")
print("hostname  is: " + hostname)


username = input("Enter username:")
print("Username is: " + username)
