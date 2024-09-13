from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    
    response = make_response(render_template('index.html'))
    response.headers["Permissions-Policy"] = "browsing-topics"
