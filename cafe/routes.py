from flask import render_template, url_for, flash, redirect
from cafe import app
from cafe.forms import FormularioRegistro, FormularioLogin
from cafe.models import Usuario, Post

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
    return render_template('index.html', titulo='Inicio', posts=posts, )

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
