from flask import Flask,request,render_template,jsonify
import numpy as np
import pandas as pd
import pickle


application=Flask(__name__)
app=application

#importing the models

standard_scaler=pickle.load(open('scaler.pkl','rb'))
ridge_model=pickle.load(open('ridge.pkl','rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    if request.method=="POST":
        Temp=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))

        stn_data=standard_scaler.transform([[Temp,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(stn_data)
        return render_template('home2.html',results=result[0])

    else:
        return render_template('home2.html')
    
    

if __name__=="__main__":
    app.run(host="0.0.0.0")