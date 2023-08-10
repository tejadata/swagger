#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:36:26 2023

@author: bhanuteja
"""

from flask import Flask,request
from flask_cors import CORS
import json
import statistics

app = Flask(__name__)
CORS(app)
@app.route("/mean",methods=['POST'])
def mean():
    
    data = json.loads(request.data)
   
    return str(data["a"]+data["b"]/2)

@app.route("/mode",methods=['POST'])
def mode():
    
    data = json.loads(request.data)
   
    return str(statistics.mode(data['a']))

@app.route("/")
def read_file():
    f = open("swagger_stats.json", "r")
    response=f.read()
   
    return response


# http://localhost/api/new_user
if __name__ == '__main__':
    app.run()
    
    
