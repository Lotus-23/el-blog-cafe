from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import FormularioRegistro, FormularioLogin

# Config
app = Flask(__name__)
app.config['SECRET_KEY'] = '31e8281c030ec4067a72fa8bdab7b098'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
isUser = False

# Database
db = SQLAlchemy(app)

class Usuario(db.Model):
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


posts = [
    {
        'autor':'Javier Rozas',
        'titulo':'Post N°1 del Blog',
        'contenido':'Condenido del primer post',
        'fecha':'19 Abril 2021'
    },
    {
        'autor':'Danae Gonzalez',
        'titulo':'Post N°2 del Blog',
        'contenido':'Condenido del segundo post',
        'fecha':'21 Abril 2021'
    },    
    ]

@app.route('/')
def blog():
    return render_template('index.html', titulo='Inicio', posts=posts, isUser=isUser)

@app.route('/post')
def post():
    return render_template('post.html')    

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = FormularioRegistro()
    if form.validate_on_submit():
        flash(f'Registro satisfactorio para el usuario { form.usuario.data }!', 'success')
        return redirect(url_for('blog'))

    return render_template('registro.html', titulo='Registro', form=form)      

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormularioLogin()
    if form.validate_on_submit():
        if form.correo.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'Ingresaste al Blog Café !', 'success')
            isUser = True
            return redirect(url_for('blog'))
        else:
            flash(f'El ingreso falló, por favor revise su nombre de usuario y contraseña', 'danger')

    return render_template('login.html', titulo='Log In', form=form)      

if __name__ == '__main__':
    app.run(debug = True)    