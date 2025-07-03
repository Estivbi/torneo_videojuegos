from flask import Blueprint, render_template, request

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

    return render_template(
        'register.html',
        email_error=email_error,
        username_error=username_error,
        password_error=password_error,
        email_valid=email_valid,
        username_valid=username_valid,
        password_valid=password_valid
    )