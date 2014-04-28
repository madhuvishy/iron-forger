from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
#from wtforms.validators import Required
 
class ProposalForm(Form):
    name = TextField('name')
    example = TextField('example')
