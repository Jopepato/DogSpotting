from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from imageai.Detection import ObjectDetection
from botocore.exceptions import ClientError
import os
import urllib.request
import boto3
import logging


def load_model():
    global execution_path
    execution_path = os.getcwd()
    global detector
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
    detector.loadModel()

def detect_dogs(imageUrl):
    urllib.request.urlretrieve(imageUrl, os.path.join(execution_path, "aux.jpg"))
    custom = detector.CustomObjects(dog=True)
    detections = detector.detectCustomObjectsFromImage(custom_objects=custom,
     input_image=os.path.join(execution_path , "aux.jpg"), minimum_percentage_probability=60,
      output_image_path=os.path.join(execution_path , "result.jpg"), input_type="file", output_type="file")
    upload_image("result.jpg")
    return detections

def upload_image(imagePath):
    # Upload the file
    client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('ACCESS_KEY'),
    aws_secret_access_key=os.getenv('SECRET_KEY'),
    )
    try:
        response = client.upload_file(imagePath, "bucket-dogspotting", "DogsResult")
    except ClientError as e:
        logging.error(e)
        return False
    return True

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/predict', methods=['POST'])
def predict_image():
    if not request.json or not 'url' in request.json:
        abort(400)
    
    imageUrl = request.json['url']
    detections = detect_dogs(imageUrl)
    listDetections =[]
    count = 0
    for eachDetection in detections:
        dog ={
            'id' : str(count),
            'probability' : str(eachDetection["percentage_probability"]),
            'bounding_box': str(eachDetection["box_points"])
        }
        listDetections.append(dog)
        count += 1
    return jsonify({'dogs': listDetections},), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    print("Loading keras model")
    load_model()
    print("Running server")
    app.run(port=80, host="0.0.0.0", threaded=False)