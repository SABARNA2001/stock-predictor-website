from flask import Flask,render_template,request
import pickle
import numpy as np


model = pickle.load(open('stock_prediction.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])

def predict_placement():
    open_price = float(request.form.get('open price'))

    result = model.predict(np.array([open_price]).reshape(1,1))



    return str(result)

if __name__ == '__main__' :

    app.run(debug=True)