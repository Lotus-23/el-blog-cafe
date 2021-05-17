from flask import render_template, url_for, flash, redirect, request
from cafe import app, db, bcrypt
from cafe.forms import FormularioRegistro, FormularioLogin
from cafe.models import Usuario, Post
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('blog'))
    form = FormularioRegistro()
    if form.validate_on_submit():
        # Encriptar contraseña
        h_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # Crear nuevo usuario y agregarlo a la BD
        usuario = Usuario(usuario=form.usuario.data, correo=form.correo.data, password=h_pass)
        db.session.add(usuario)
        db.session.commit()
        # Mensaje satisfactorio y redirect a login
        flash(f'Su cuenta ha sido creada ya puede ingresar al blog Café', 'success')
        return redirect(url_for('login'))

    return render_template('registro.html', titulo='Registro', form=form)      

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog'))
    form = FormularioLogin()
    if form.validate_on_submit():
        user = Usuario.query.filter_by(correo=form.correo.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.recuerdame.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('blog'))
        else:
            flash(f'El ingreso falló, por favor revise su nombre de usuario y contraseña', 'danger')
    return render_template('login.html', titulo='Log In', form=form)      

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('blog'))

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html', titulo='Perfil')