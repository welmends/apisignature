from config import Config
from signature import SigBackRemoval
import sys
import json
from flask import Flask,request, jsonify, render_template
from flask_cors import CORS, cross_origin

### Flask Config ###
app = Flask(__name__)
app.config['DEBUG'] = False
CORS(app)

### Routes ###
@app.route('/', methods=['GET'], endpoint=Config.ENDPOINT)
def apicovid19predict():
    return 'im alive'

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