from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@views.route('/perfil', methods=['GET'])
def perfil():
    return render_template('perfil.html')

@views.route('/login', methods=['GET'])
def login():
    return render_template('inciosesion.html')



