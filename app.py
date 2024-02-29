from flask import Flask,render_template,request
import os
import numpy as np
import pandas as pd

from src.Project4.pipeline.prediction import PredictionPipeline

app = Flask(__name__)


@app.route('/',methods=['GET'])
def homepage():
    return render_template('index.html')


@app.route('/train',methods=['GET'])
def train():
    os.system('python main.py')
    return 'Training Successful!'


@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        try:
            age = int(request.form['age'])
            sex = int(request.form['sex'])
            cp = int(request.form['cp'])
            trtbps = int(request.form['trtbps'])
            chol = int(request.form['chol'])
            fbs = int(request.form['fbs'])
            restecg = int(request.form['restecg'])
            thalachh = int(request.form['thalachh'])
            exng = int(request.form['exng'])
            oldpeak = float(request.form['oldpeak'])
            slp = int(request.form['slp'])
            caa = int(request.form['caa'])
            thall = int(request.form['thall'])
            
            data = [age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]
            data = np.array(data).reshape(1,13)
            
            obj = PredictionPipeline()
            predict = obj.predict(data=data)
            return render_template('result.html',prediction=str(predict))
        
        except Exception as e:
            raise e
    else:
        # If request method is GET, render the prediction form
        return render_template('prediction.html')


if __name__=='__main__':
    # app.run(host='0.0.0.0',port=8000,debug=True)
    app.run(host='0.0.0.0',port=8000)
