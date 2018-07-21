from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField
app = Flask(__name__)

app.config['SECRET_KEY'] = '123456789'

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')


@app.route('/', methods=['GET','POST'])
@app.route('/home', methods=['GET','POST'])
def my_sort(name = None):
	if request.method == 'POST':
		text = request.form['text']
		input_list = text.split()
		input_list.sort()
		final_return = ', '.join(input_list)
		final_return.__str__()

		return render_template('home.html', name=final_return)



@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)


@app.route('/google')
def google():
	return redirect('https://www.google.com')

if __name__ == '__main__':
	app.run(debug=True)