from config import Config
from signature import SigBackRemoval
import sys
import json
import io
import cv2 as cv
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

### Flask Config ###
sbr = SigBackRemoval()
app = Flask(__name__)
app.config['DEBUG'] = False
CORS(app)

### Routes ###
@app.route('/', methods=['GET'])
def init():
    return '<h1>Service of signature background removal implemented with Flask</h1>'

@app.route("/signature", methods=["POST"])
def process():
    # Usage: curl http://localhost:9999/signature -X POST -F image=@/path/to/image
    image_request = request.files["image"]
    image_bytes = io.BytesIO(image_request.read())
    file_bytes = np.asarray(bytearray(image_bytes.read()), dtype=np.uint8)
    image = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
    output = sbr.process_signature(image)
    cv.imwrite("/Users/well/Desktop/img.png", output)
    return 'Processed\n'

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