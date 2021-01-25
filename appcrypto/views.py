from appcrypto import app
from flask import render_template

@app.route('/')
def cryptoMovements():
    return render_template('cryptoMovements.html')
