from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length, ValidationError
from wtforms.fields.html5 import EmailField
from cafe.models import Usuario

class FormularioRegistro(FlaskForm):

    usuario = StringField('Nombre de Usuario', validators=[InputRequired("Por favor ingrese su nombre de usuario"), Length(min=3, max=20)])
    correo = EmailField('Email', validators=[InputRequired("Por favor ingrese su correo electrónico"), Email()])
    password = PasswordField('Contraseña', validators=[InputRequired("Por favor ingrese su contraseña")])
    confirma_password = PasswordField('Confirme su Contraseña', validators=[InputRequired("Por favor vuelva a ingresasr su contraseña"), EqualTo('password')])

    enviar = SubmitField('Regístrate!')

    def validate_usuario(self, usuario):
        
        user = Usuario.query.filter_by(usuario=usuario.data).first()
        if user:
            raise ValidationError('Este nombre de usuario ya está en uso, por favor ingrese uno diferente')

    def validate_correo(self, correo):
        
        user = Usuario.query.filter_by(correo=correo.data).first()
        if user:
            raise ValidationError('Este correo electrónico ya está en uso, por favor ingrese uno diferente')


class FormularioLogin(FlaskForm):

    correo = EmailField('Email', validators=[InputRequired("Por favor ingrese su correo electrónico"), Email()])
    password = PasswordField('Contraseña', validators=[InputRequired("Por favor ingrese su contraseña") ])
    recuerdame = BooleanField('Recuérdame')

    enviar = SubmitField('Ingresar')    

class DataUpdateForm(FlaskForm):

    usuario = StringField('Nombre de Usuario', validators=[InputRequired("Por favor ingrese su nombre de usuario"), Length(min=3, max=20)])
    correo = EmailField('Email', validators=[InputRequired("Por favor ingrese su correo electrónico"), Email()])
    imagen = FileField('Cambiar Avatar', validators=[FileAllowed(['jpg', 'png'])])

    enviar = SubmitField('Actualiza tus datos')

    def validate_usuario(self, usuario):
        if usuario.data != current_user.usuario:
            user = Usuario.query.filter_by(usuario=usuario.data).first()
            if user:
                raise ValidationError('Este nombre de usuario ya está en uso, por favor ingrese uno diferente')

    def validate_correo(self, correo):
        if correo.data != current_user.correo:
            user = Usuario.query.filter_by(correo=correo.data).first()
            if user:
                raise ValidationError('Este correo electrónico ya está en uso, por favor ingrese uno diferente')
