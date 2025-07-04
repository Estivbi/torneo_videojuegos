from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from models import get_db

main = Blueprint('main', __name__)

@main.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    db = get_db()
    # Partidas del usuario
    user_games = db.execute(
        'SELECT m.*, g.name as game_name FROM matches m JOIN games g ON m.game_id = g.id WHERE m.user_id = ?',
        (session['user_id'],)
    ).fetchall()

    # Ranking por puntos (High Score)
    ranking_puntos = db.execute(
        '''SELECT u.username, MAX(m.score) as max_score
           FROM matches m JOIN users u ON m.user_id = u.id
           WHERE m.game_id = 2
           GROUP BY m.user_id
           ORDER BY max_score DESC
           LIMIT 10'''
    ).fetchall()

    # Ranking por tiempo (Speed Run)
    ranking_tiempo = db.execute(
        '''SELECT u.username, MIN(m.time) as min_time
           FROM matches m JOIN users u ON m.user_id = u.id
           WHERE m.game_id = 1 AND m.time > 0
           GROUP BY m.user_id
           ORDER BY min_time ASC
           LIMIT 10'''
    ).fetchall()

    # Estadísticas básicas
    games_played = len(user_games)
    wins = sum(1 for g in user_games if g['result'] and g['result'].lower() == 'victoria')
    ranking = 'N/A'
    progress = 40

    stats = {
        'games_played': games_played,
        'wins': wins,
        'ranking': ranking,
        'progress': progress
    }

    games = []
    for g in user_games:
        games.append({
            'name': g['game_name'],
            'date': g['date'] if 'date' in g.keys() else 'N/A',
            'result': g['result'] or 'Sin resultado'
        })

    return render_template(
        'dashboard.html',
        games=games,
        stats=stats,
        ranking_puntos=ranking_puntos,
        ranking_tiempo=ranking_tiempo
    )
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/registrar_partida', methods=['GET', 'POST'])
def registrar_partida():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    db = get_db()
    juegos = db.execute('SELECT * FROM games').fetchall()

    if request.method == 'POST':
        game_id = request.form['game_id']
        level = request.form['level']
        score = request.form['score']
        time = request.form['time']
        result = request.form['result']

        db.execute(
            'INSERT INTO matches (user_id, game_id, level, score, time, result) VALUES (?, ?, ?, ?, ?, ?)',
            (session['user_id'], game_id, level, score, time, result)
        )
        db.commit()
        flash('Partida registrada correctamente.', 'success')
        return redirect(url_for('main.dashboard'))

    return render_template('registrar_partida.html', juegos=juegos)