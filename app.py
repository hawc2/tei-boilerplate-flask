from flask import Flask, flash, redirect, render_template, request, session, abort

def create_app(test_config=None):
	app = Flask(__name__)

	@app.route('/')
	def index():
	    return render_template('index.html')

	@app.route('/tei')
	def hello():
	    return render_template('tei.html')

	return app