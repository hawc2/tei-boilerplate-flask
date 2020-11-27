from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tei')
def tei():
    return render_template('BeggarsOpera.xml')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
