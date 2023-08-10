from flask import Flask,request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
@app.route("/add",methods=['POST'])
def add():
    
    data = json.loads(request.data)
   
    return str(data["a"]+data["b"])

@app.route("/sub",methods=['POST'])
def sub():
    
    data = json.loads(request.data)
   
    return str(data["a"]-data["b"])

@app.route("/mul",methods=['POST'])
def mul():
    
    data = json.loads(request.data)
   
    return str(data["a"]*data["b"])

@app.route("/div",methods=['POST'])
def div():
    
    data = json.loads(request.data)
   
    return str(data["a"]/data["b"])

@app.route("/")
def read_file():
    f = open("swagger.json", "r")
    response=f.read()
   
    return response

# http://localhost/api/new_user
if __name__ == '__main__':
    app.run()
    
    
