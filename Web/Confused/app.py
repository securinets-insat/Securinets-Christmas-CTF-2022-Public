# -*- coding:utf-8 -*-
from flask import Flask,request,jsonify
import os
app = Flask(__name__)

posts=[
{"id":0,"content":"So Secret data only admin have to visit it, wait how are you reading me :o"}, # PRIVATE NOTE #
{"id":1,"content":"Congraaats!! "+os.environ.get("FLAG")}, # PRIVATE NOTE #
{"id":2,"content":"Naruto is really awesome, so i'am x) "}, # PRIVATE NOTE #
{"id":3,"content":"Your Lie in April is really sad"},
{"id":4,"content":"I'm happy without any reason"},
{"id":5,"content":"I have no idea what i'm doing"}
]

def is_Super_Admin():
## You are not a super Admin for sure :) ##
	return False 

@app.route("/source",methods=["GET"])
def source():
	return '<pre class="brush: python">'+open("./app.py").read()+"</pre>"

@app.route("/posts",methods=["POST"])
def list_posts():
	id=int(request.json["id"])
	if is_Super_Admin() or request.json["id"]>len(posts)-4:
		return jsonify(posts[id])
	else:
		return jsonify({"result":"Forbidden! What's interesting about my private notes :("})


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=1234,debug=False)
