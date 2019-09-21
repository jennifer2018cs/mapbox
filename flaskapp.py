from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'cb4857b56db25f4c2d0ae36edbea7902'

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', title="Home")

@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.username.data == 'admin' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)