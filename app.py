from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from ChickenClassf.utils.common import decodeImage
from ChickenClassf.pipeline.predict import PredictPipeline


os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)   #we can request from othr domoain

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictPipeline(self.filename)
        
        
@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/train',methods=['GET','POST'])  #to train model again
@cross_origin()
def train_image():
    os.system('python dvc.yaml')
    return 'Traing model completed'

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
    input_image= request.json['image']
    decodeImage(input_image,clapp.filename)
    result= clapp.classifier.Predict()
    
    return jsonify(result)

if __name__ == '__main__':
    clapp = ClientApp()
    app.run(host='0.0.0.0', port=8080,debug=True)
    
    
    
    

        
        

