from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ycictymerruaju:e21852668f6cc9a430847840d21559dc2da4600d05bde1cc6642b5ae9b9f49a3@ec2-54-204-40-248.compute-1.amazonaws.com:5432/d79uoekomvergl' #Not secure, I know. Just doing this for the demo project. 

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

@app.route('/')
def home():
        return render_template('home.html')

@app.route('/collections', methods=['POST'])
def collections():
    email = None
    if request.method == 'POST':
        email = request.form['email']
        reg = User(email)
        db.session.add(reg)
        db.session.commit()
        return render_template('success.html')
    return render_template("home.html")

@app.route('/return_emails', methods=['GET'])
def return_emails(): 
    all_emails = db.session.query(User.email).all()
    return jsonify(all_emails)

if __name__ == "__main__": 
    app.debug = True
    app.run()