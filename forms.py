from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DecimalField
from wtforms.validators import DataRequired

class MakeObject(FlaskForm):
    name = StringField("Name of product: ", validators=[DataRequired()])
    url = StringField("URL of product: ", validators=[DataRequired()])
    target_price = DecimalField("Target price of product: ", validators=[DataRequired()])
    submit = SubmitField("Add")