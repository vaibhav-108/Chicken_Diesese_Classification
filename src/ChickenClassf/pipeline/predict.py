import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
import os


class PredictPipeline:
    def __init__(self, filename):
        self.filename = filename
        
    def Predict(self):
        model =load_model(os.path.join('artifacts','training','model.keras'))
        
        image_file = image.load_img(self.filename, target_size=(224,224))
        test_image = image.img_to_array(image_file)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image),axis=1)
        
        print(result)
        
        if result[0] == 1:
            prediction = 'Healthy'
            return [{'Image': prediction}]
            
        else:
            prediction = 'Diseased'
            return [{'Image': prediction}]
    
        
                