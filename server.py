from config import Config
from signature import SigBackRemoval
import sys
import io
import base64
import cv2 as cv
import numpy as np
from flask import Flask, request, jsonify, render_template

### Flask Config ###
sbr = SigBackRemoval()
app = Flask(__name__)
app.config['DEBUG'] = False
base64img = None

### Routes ###
@app.route('/', methods=['GET'])
def init():
    return '<h1>Service of signature background removal implemented with Flask</h1>'

@app.route('/apisignature/process', methods=['POST'])
def process():
    global base64img
    image_request = request.files['image']
    image_bytes = io.BytesIO(image_request.read())
    file_bytes = np.asarray(bytearray(image_bytes.read()), dtype=np.uint8)
    image = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
    image_processed = sbr.process_signature(image)
    retval, buffer = cv.imencode('.png', image_processed)
    image_base64 = base64.b64encode(buffer).decode("utf-8")
    return image_base64

@app.route('/apisignature/process_view', methods=['POST'])
def process():
    global base64img
    image_request = request.files['image']
    image_bytes = io.BytesIO(image_request.read())
    file_bytes = np.asarray(bytearray(image_bytes.read()), dtype=np.uint8)
    image = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
    image_processed = sbr.process_signature(image)
    retval, buffer = cv.imencode('.png', image_processed)
    image_base64 = base64.b64encode(buffer).decode("utf-8")
    base64img = image_base64
    return 'http://{}:{}/apisignature/view\n'.format(Config.HOST,Config.PORT)

@app.route('/apisignature/view', methods=['GET'])
def retrieve():
    global base64img
    html_1 = '<div><img src="data:image/png;base64, '
    html_2 = ' " alt="signature.png"/></div>'
    image_base64 = base64img
    base64img = None
    if image_base64==None:
        return '<h1>No signature available</h1>'
    else:
        return html_1+image_base64+html_2

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