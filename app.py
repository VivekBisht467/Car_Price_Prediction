from flask import Flask, render_template, request
import requests
from joblib import dump, load

app = Flask(__name__)
model = load('pipeline.joblib')
@app.route('/',methods=['GET'])
def Home():
    return render_template('front.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        CRIM = request.form['CRIM']
        ZN=float(request.form['ZN'])
        INDUS=float(request.form['INDUS'])
        CHAS=request.form['CHAS']
        if(CHAS=='Tract bounds River'):
              CHAS = 1  
        else:
            CHAS = 0
        NOX=float(request.form['NOX'])
        RM=float(request.form['RM'])
        AGE=float(request.form['AGE'])
        DIS = float(request.form['DIS'])
        RAD = float(request.form['RAD'])
        TAX = float(request.form['TAX'])
        PTRATIO = float(request.form['PTRATIO'])
        B = float(request.form['B'])
        LSTAT = float(request.form['LSTAT'])
        prediction=model.predict([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('front.html',prediction_texts="Sorry you cannot sell this House")
        else:
            return render_template('front.html',prediction_text="Price of house {} ($1000's)".format(output))
    else:
        return render_template('front.html')

if __name__=="__main__":
    app.run(debug=True)

