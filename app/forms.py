from wtforms import Form, StringField, PasswordField, validators, TextAreaField


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


class RegisterForm(Form):
    what_to_get = TextAreaField(label='What to get', validators=[validators.InputRequired()])
    what_not_to_get = TextAreaField(label='What not to get', validators=[validators.InputRequired()])
    who_to_ask_for_help = TextAreaField(label='Who to ask for help', validators=[validators.InputRequired()])
