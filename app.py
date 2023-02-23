import pickle
from flask import Flask, request, app, jsonify, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
## load model
regmodel = pickle.load(open('regmodelrfr.pkl','rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    submitted = False
    if request.method == 'POST':
        submitted = True
        data = [float(x) for x in request.form.values()]
        final_input = scalar.transform(np.array(data).reshape(1,-1))
        print(final_input)
        output = round(regmodel.predict(final_input)[0], 5)
    return render_template("home.html", submitted=submitted, prediction_text = "The House Price Predict is ${}".format(output), target='#result')

if __name__ == "__main__":
    app.run(debug=True)