from flask import Flask , render_template , request
import numpy as np
import pickle
app=Flask(__name__)
model1 = pickle.load(open('model1.pkl','rb'))
@app.route('/')
def home():
    return render_template('weather.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    MaxtempC = request.form.get('MaxtempC')
    MintempC = request.form.get('MintempC')
    humidity = request.form.get('humidity')
    Pressure = request.form.get('Pressure')
    SunHour = request.form.get('SunHour')
    heat = request.form.get('heat')
    wind = request.form.get('wind')
    Result =model1.predict([[MaxtempC, MintempC,humidity, SunHour, heat, Pressure, wind]])
    return render_template('result.html',**locals())
if __name__ == '__main__':
    app.run(debug=True)