from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TrainingForm(FlaskForm):
    name = StringField('Training Name', validators=[DataRequired()])
    submit = SubmitField('Add Training')
