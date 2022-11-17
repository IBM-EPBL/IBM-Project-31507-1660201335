#import the packages
from flask import Flask, render_template,request
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model 

app=Flask(__name__,template_folder='template')

#index page load
@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

#load the  main page 
@app.route("/main",methods=['GET'])
def main():
    return render_template("main.html")

# get the image in app.py and predict the image
@app.route("/main",methods=['POST'])
def upload():

# already trained model as been save this code load the model here
    model = load_model('model/mnistCNN.h5')



#image is preproceesing and predicte the image
    imagefile = request.files['imagefile']
    if imagefile:
        img = Image.open(request.files['imagefile'].stream).convert("L")
        img = img.resize((28,28))
        image = np.array(img)
        image = image.reshape(1,28,28,1)
        prid = model.predict(image)
        prid =np.argmax(prid,axis= 1)

# predict the image and if condition using load the html page 
        if (int(prid) == 0):
            return render_template("zero.html")
        if (int(prid)== 1):
            return render_template("one.html")
        if (int(prid)== 2):
            return render_template("two.html")
        if (int(prid)== 3):
            return render_template("three.html")          
        if (int(prid)== 4):
            return render_template("four.html")  
        if (int(prid)== 5):
            return render_template("five.html")  
        if (int(prid)== 6):
            return render_template("six.html")  
        if (int(prid)== 7):
            return render_template("seven.html")  
        if (int(prid)== 8):
            return render_template("eight.html")  
        if (int(prid)== 9):
            return render_template("nine.html")  
    else:
        return render_template("main.html")
if __name__=='__main__':
    app.run(debug=True)