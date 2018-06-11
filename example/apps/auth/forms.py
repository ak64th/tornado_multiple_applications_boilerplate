from wtforms_tornado import Form
from wtforms.fields import StringField
from wtforms.validators import DataRequired


class LoginForm(Form):
    app_key = StringField(validators=[DataRequired()])
    username = StringField(validators=[DataRequired()])
    password = StringField(validators=[DataRequired()])
