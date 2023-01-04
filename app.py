#!flask/bin/python 
from flask import Flask, jsonify, request 
app = Flask(__name__) 


@app.route("/", methods=["GET"])' 
def print_client_ip(): 
    return jsonify({'ip': request.remote_addr}), 200" 
