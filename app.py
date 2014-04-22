from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/proposal')
def vote():
    return "List of proposals goes here"

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


