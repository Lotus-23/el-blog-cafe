from flask import Flask, render_template, url_for
from forms import FormularioRegistro, FormularioLogin
app = Flask(__name__)

app.config['SECRET_KEY'] = '31e8281c030ec4067a72fa8bdab7b098'

isUser = False

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
    return render_template('index.html', titulo='Inicio', posts=posts, isUser=False)

@app.route('/post')
def post():
    return render_template('post.html')    

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = FormularioRegistro()
    return render_template('registro.html', titulo='Registro', form=form)      

@app.route('/login')
def login():
    form = FormularioLogin()
    return render_template('login.html', titulo='Log In', form=form)      

if __name__ == '__main__':
    app.run(debug = True)    