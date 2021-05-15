from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, InputRequired
from wtforms.fields.html5 import EmailField

class FormularioRegistro(FlaskForm):

    usuario = StringField('Nombre de Usuario', validators=[InputRequired("Por favor ingrese su nombre de usuario"), Length(min=3, max=20)])
    correo = EmailField('Email', validators=[InputRequired("Por favor ingrese su correo electrónico"), Email()])
    password = PasswordField('Contraseña', validators=[InputRequired("Por favor ingrese su contraseña")])
    confirma_password = PasswordField('Confirme su Contraseña', validators=[InputRequired("Por favor vuelva a ingresasr su contraseña"), EqualTo('password')])

    enviar = SubmitField('Regístrate!')


class FormularioLogin(FlaskForm):

    correo = EmailField('Email', validators=[InputRequired("Por favor ingrese su correo electrónico"), Email()])
    password = PasswordField('Contraseña', validators=[InputRequired("Por favor ingrese su contraseña") ])
    recuerdame = BooleanField('Recuérdame')

    enviar = SubmitField('Ingresar')    