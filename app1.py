from flask import Flask, render_template,request
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))
app= Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict_placement():
    CGPA= float(request.form.get('CGPA'))
    IQ = int(request.form.get('IQ'))
    Profile_Score = int(request.form.get('Profile_Score'))
    result=model.predict(np.array([CGPA,IQ,Profile_Score]).reshape(1,3))
    if result[0]==1:
        result ="You will be PLACED!!"
    else:
        result ="Sorry, you will NOT be placed :( :("
    return render_template('index.html',result=result)
if __name__=='__main__':
    app.run(debug=True)