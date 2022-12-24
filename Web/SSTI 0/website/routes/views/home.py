from .route import web
from flask import Flask, request, render_template_string

@web.route('/')
def hello():
    if not request.args.get('name'):
        name = "mohsen"
        return f'<html><head><title>SSTI0</title><body>My job is simple, you give me your ?name="your name" and I \' ll say Hello, {name}! .. if your name is mohsen ofc.</body></head></html>'


    name = render_template_string(request.args.get('name'))
    return f'<html><head><title>SSTI0</title><body>My job is simple, you give me your ?name="your name" and I \' ll say Hello, {name}! .. they pay me 1$ per greeting so yeah.</body></head></html>'

