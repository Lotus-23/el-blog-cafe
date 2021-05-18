import os 
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from cafe import app, db, bcrypt
from cafe.forms import FormularioRegistro, FormularioLogin, DataUpdateForm
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

def guardar_img(form_img):
    random_hex = secrets.token_hex(16)
    _, f_ext = os.path.splitext(form_img.filename)
    img_fn = random_hex + f_ext
    path_img = os.path.join(app.root_path, 'static/user_img', img_fn)
    size = (125, 125)
    i = Image.open(form_img)
    i.thumbnail(size)
    i.save(path_img)

    return img_fn

@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
    form = DataUpdateForm()
    if form.validate_on_submit():
        if form.imagen.data:
            img_file = guardar_img(form.imagen.data)
            current_user.avatar = img_file
        current_user.usuario = form.usuario.data
        current_user.correo = form.correo.data
        db.session.commit()
        flash('Su cuenta ha sido actualizada!', 'success')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        form.usuario.data = current_user.usuario
        form.correo.data = current_user.correo

    avatar = url_for('static', filename='user_img/'+current_user.avatar)
    return render_template('perfil.html', titulo='Perfil', avatar=avatar, form=form)