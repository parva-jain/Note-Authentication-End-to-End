#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:27:35 2021

@author: parv
"""


from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"


@app.route('/predict')
def predict_note_authentication():
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    return 'The prediction value is ' + str(prediction)


@app.route('/predict_file', methods=['POST'])
def predict_note_file():
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return 'The prediction values for the csv is ' + str(list(prediction))










if __name__ == '__main__':
    app.run()