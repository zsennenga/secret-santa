from wtforms import Form, StringField, PasswordField, validators


class LoginForm(Form):
    email = StringField(label='Email', validators=[validators.InputRequired()])
    password = PasswordField(label='Password', validators=[validators.InputRequired()])


class SignupForm(Form):
    name = StringField('Name', validators=[validators.InputRequired()])
    email = StringField(
        label='Email',
        validators=[
            validators.InputRequired(),
            validators.length(max=256),
            validators.Email()
        ]
    )
    password = PasswordField(
        label='Password',
        validators=[
            validators.InputRequired(),
            validators.length(min=6, max=70),
        ],
    )
