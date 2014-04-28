from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, RadioField
#from wtforms.validators import Required
 
class ProposalForm(Form):
    name = TextField('name')
    example = TextField('example')

class VoteForm(Form):
    vote_choice = RadioField("boat", choices=[("yay", "Yay!"), 
            ("meh", "Meh."), ("ugh", "Ugh.")])