from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)

users = {"adam":"adam123", "loai":"loai123", "jameel":"jameel123"}
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]


@app.route('/', methods=["GET", "POST"])  # '/' for the default page
def login():
	if request.method == "POST":
		name_f = request.form["username"].lower()
		password_f = request.form["password"]
		try:
			if users[name_f] == password_f:
				return redirect(url_for('home'))
		except:
			pass
	return render_template('login.html')

@app.route('/home')
def home():
	return render_template('home.html', friends = facebook_friends)


@app.route('/friend_exists/<string:name>')
def friend_exists(name):
	flag = False
	if name in facebook_friends:
		flag = True
	return render_template('friend_exists.html', flag = flag)



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)