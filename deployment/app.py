from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

model = load_model('Trained.h5')

def return_prediction(model, image):
    
    # Preprocess image
    img = Image.open(image).convert('RGB').resize((83, 83))
    img = np.array(img).reshape(1, 83, 83, 3)/255
    
    # Predict the class
    classes = ['laptop', 'phone']
    pred = model.predict(img)
    class_ind = round(pred[0][0])
    
    # return prediction
    return classes[class_ind]
    
    
 ####### Start of the App
 
app = Flask(__name__)
 
 
@app.route("/")
def index():
    return render_template('upload.html')
    
@app.route("/uploader", methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':

		# storing file
		#f = request.files['file']
		#fname = secure_filename(f.filename)
		#f.save("assests/" + fname)

		# prediction
		result = return_prediction(model, request.files['file'])#"assests/" + fname)
		return result
	return "nothing"



    
if __name__ == '__main__':
	app.run()
