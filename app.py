from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ''

@app.route('/')
def home():
        return "<h1>Welcome</h1>"


if __name__ == "__main__": 
    app.debug = True
    app.run()