from flask import Flask, render_template
import json

app = Flask("Portfolio")


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/images')
def images():
	return render_template('images.html')

@app.route('/page1')
def page1():
	return render_template('page1.html')

@app.route('/page2')
def page2():
	return render_template('page2.html')

@app.route('/page3')
def page3():
	return render_template('page3.html')


if __name__ == "__main__":
	app.run(port = 8000, debug = True)