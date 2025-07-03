from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models import add_user, get_user, create_user_table
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__)

@auth.before_app_first_request
def init_db():
    create_user_table()

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if get_user(username):
            flash('El usuario ya existe.')
            return redirect(url_for('auth.register'))
        add_user(username, password)
        flash('Registro exitoso. Inicia sesión.')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = get_user(username)
        if user and check_password_hash(user['password'], password):
            session['user_id'] = user['id']
            session['is_admin'] = user['is_admin']
            return redirect(url_for('main.index'))
        flash('Usuario o contraseña incorrectos.')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))