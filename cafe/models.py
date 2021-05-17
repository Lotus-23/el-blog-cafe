from datetime import datetime
from cafe import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String(20), unique = True, nullable = False)
    correo = db.Column(db.String(120), unique = True, nullable = False)
    avatar = db.Column(db.String(20), nullable = False, default = 'default.jpeg')
    password = db.Column(db.String(60), nullable = False)
    posteos = db.relationship('Post', backref = 'autor', lazy = True)

    def __repr__(self):
        return f"Usuario('{self.usuario}, {self.correo}, {self.avatar}, ')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100), nullable = False)
    fecha_posteo = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    contenido = db.Column(db.Text, nullable = False, )
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    
    def __repr__(self):
        return f"Post('{self.titulo}, {self.fecha_posteo}, ')"
