import json
from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from werkzeug.wrappers import request
from flask import flash, request

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@views.route('/perfil', methods=['GET'])
def perfil():
    return render_template('perfil.html')

@views.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@views.route('/camaras', methods=['GET'])
def camaras():
    return render_template('camaras.html')

@views.route('/medicamentos', methods=['GET'])
def medicamentos():
    return render_template('medicamentos.html')

@views.route('/musicoterapia', methods=['GET'])
def musicoterapia():
    return render_template('musicoterapia.html')





