import flask
from logic import get_message, get_guild, get_user_info, get_channel
# sudo pip3 install flask
# On any hosting machine
from flask import Flask, render_template, redirect, url_for, request, session
import os
import random

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')
		
@app.route("/login", methods=['GET', 'POST'])
def login():
	pass

@app.route("/showcase")
def showcase():
	return render_template('showcase.html')

@app.route("/joinus")
def joinus():
	return render_template("joinus.html")

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0", port=8080)
