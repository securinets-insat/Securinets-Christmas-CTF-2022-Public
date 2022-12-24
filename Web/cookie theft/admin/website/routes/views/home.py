from .route import web
from flask import render_template, request, Response
import re
import requests
import pyodbc
import threading
import os
import sys

CSP= [
"base-uri 'self'",
"frame-ancestors 'none'",
"img-src 'self'",
"object-src 'none'",
"script-src 'self' 'unsafe-eval' https://*.google.com/ https://kit.fontawesome.com/",
"style-src 'self' 'unsafe-inline' https://fonts.googleapis.com/",
]




@web.route('/', defaults={'name': ''})
@web.route('/<name>',methods = ['GET'])
def home(name):
    if not name:
        name = "samurai"
    resp = Response((render_template("dashboard.html", name=name)))
    resp.headers['Content-Security-Policy'] = ';'.join(CSP)
    return resp



