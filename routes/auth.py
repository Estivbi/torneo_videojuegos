from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import get_db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    email_error = username_error = password_error = None
    email_valid = username_valid = password_valid = False
    username_error = password_error = None
    username_valid = password_valid = False

    if request.method == 'POST':
        email = request.form.get('email', '')
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        if not email or '@' not in email or '.' not in email:
            email_error = 'Por favor ingresa un correo válido.'
        else:
            email_valid = True

        if not username or len(username) < 3:
            username_error = 'El usuario debe tener al menos 3 caracteres.'
        else:
            username_valid = True

        if not password or len(password) < 8:
            password_error = 'La contraseña debe tener al menos 8 caracteres.'
        else:
            password_valid = True

    # Si todo es válido, guardar en la base de datos
    if email_valid and username_valid and password_valid:
        db = get_db()
        # Verifica si el email o username ya existen
        user = db.execute(
            'SELECT id, username, email FROM users WHERE username = ? OR email = ?',
            (username, email)
        ).fetchone()
        if user:
            if user and user['username'] == username:
                username_error = 'El nombre de usuario ya está registrado.'
            if user and user['email'] == email:
                email_error = 'El correo ya está registrado.'
        else:
            try:
                db.execute(
                    'INSERT INTO users (email, username, password) VALUES (?, ?, ?)',
                    (email, username, password)
                )
                db.commit()
                flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
                return redirect(url_for('auth.login'))
            except Exception as e:
                email_error = f'Error al registrar: {str(e)}'

    return render_template(
        'register.html',
        email_error=email_error,
        username_error=username_error,
        password_error=password_error,
        email_valid=email_valid,
        username_valid=username_valid,
        password_valid=password_valid
    )