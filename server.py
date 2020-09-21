from config import Config
from signature import SigBackRemoval
import sys
import json
import flask
from flask import request, jsonify, render_template
from flask import Flask
from flask_cors import CORS, cross_origin
sys.path.append('templates')

### Flask Config ###
app = flask.Flask(__name__)
CORS(app)
app.config['DEBUG'] = False

### Routes ###
# http://localhost:3012
@app.route('/', methods=['GET'], endpoint=Config.ENDPOINT)
def apicovid19predict():
    return "i'm alive"

### Main ###
if __name__ == '__main__':
    if len(sys.argv) is not 2:
        print('Usage: python3 server.py [debug/release]')
    else:
        status = sys.argv[1]
        if status == 'debug':
            app.run()
        elif status == 'release':
            app.run(host=Config.HOST, port=Config.PORT)
        else:
            print('Error: parameter must be [debug/release]')