from pymongo import *
from flask import Flask, render_template

import os

app = Flask(__name__)

conn = MongoClient(os.environ["MONGOHQ_URL"])
db = conn.app24464341
proposals = db.proposals

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/proposal')
def vote():
    props = proposals.find()
    return render_template("proposal.html", title="Proposals", proposals=props)

@app.route('/proposal/new')
def new_proposal():
    return render_template("proposal_new.html")

@app.route('/proposal/<name>')
def proposal_name(name):
    return "proposal %s" % name

@app.route('/user')
def register():
    return "Register for an awesome account!"

@app.route('/user/<name>')
def user_name(name):
    return "user %s" % name

@app.route('/project/<name>')
def project_name(name):
    return "project %s" % name


