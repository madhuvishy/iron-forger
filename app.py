from pymongo import *
from flask import Flask

app = Flask(__name__)

conn = MongoClient('mongodb://iron-forger:foobar@oceanic.mongohq.com:10059/app24464341')
db = conn.app24464341
proposals = db.proposals

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/proposal')
def vote():
    result = "<ul>"
    props = proposals.find()
    for prop in props:
        result += "<li>%s %s %s </li>" % (prop["name"], prop["example"], prop["votes"])
    result += "</ul>"
    return result

@app.route('/proposal/new')
def new_proposal():
    return "Submit a proposal!"

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

if __name__ == '__main__':
    app.run(debug=True)


