import flask
# sudo pip3 install flask
# On any hosting machine
from flask import Flask, render_template, redirect, url_for, request, session
import os

app = Flask(__name__)

@app.route("/")
def main():
	if not session.get('logged_in'):
		return render_template('showcase.html')
	else:
		return render_template('index.html')
@app.route("/login", methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin': #change this to the value json thing that is on the webapps
			error = 'Invalid Auths. Please try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route("/joinus")
def joinus():
	return render_template("joinus.html")

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True, host="0.0.0.0", port=8080)
