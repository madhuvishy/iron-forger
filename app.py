from pymongo import *
from flask import Flask, render_template, request, redirect
from forms import ProposalForm, VoteForm

import os

app = Flask(__name__)

conn = MongoClient(os.environ["MONGOHQ_URL"])
db = conn.app24464341
proposals = db.proposals

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/proposal', methods=['GET', 'POST'])
def vote():
    props = proposals.find()
    radio_forms = {}
    for prop in props:
        radio_forms[prop["name"]] = VoteForm(request.form, csrf_enabled=False)
        updated_votes = {}
        #if request.method == 'POST':
        #    pass
        # updated_votes["yay"] = form.fields[prop["name"]].data
        # propsals.update({
        #     "name" : prop['name']
        #     },
        #     {"votes" : prop['votes']})
        # temp[prop["name"]] = form.fields[prop].data
    props.rewind()
    return render_template("proposal.html", title="Proposals", proposals=props, radio_forms=radio_forms)

@app.route('/proposal/new', methods=['GET','POST'])
def new_proposal():
    form = ProposalForm(request.form, csrf_enabled=False)
    if request.method == 'POST':
        proposals.insert({
            "name": form.name.data,
            "example": form.example.data,
            "votes": {"yay" : 0, "meh" : 0, "ugh" : 0}
        })
        return redirect("/proposal")
    return render_template("proposal_new.html", title="New Proposal", form=form)

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
