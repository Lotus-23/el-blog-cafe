from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class FormularioRegistro(FlaskForm):

    usuario = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=3, max=20)])
    #correo = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirma_password = PasswordField('Confirme su Contraseña', validators=[DataRequired(), EqualTo('password')])

    enviar = SubmitField('Regístrate!')


class FormularioLogin(FlaskForm):

    #correo = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    recuerdame = BooleanField('Recuérdame')

    enviar = SubmitField('Ingresar')    