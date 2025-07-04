from flask import Blueprint, render_template, session, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    # Aquí deberías obtener los juegos/partidas y estadísticas del usuario desde la base de datos
    user_games = []  # Reemplaza con consulta real
    stats = {}       # Reemplaza con consulta real
    return render_template('dashboard.html', games=user_games, stats=stats)

@main.route('/')
def index():
    return render_template('index.html')