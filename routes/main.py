from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from models import get_db
from functools import wraps

main = Blueprint('main', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session or session.get('role') != 'admin':
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

@main.route('/admin')
@admin_required
def admin_panel():
    return render_template('admin.html')

@main.route('/admin/usuarios')
@admin_required
def admin_usuarios():
    db = get_db()
    q = request.args.get('q', '').strip()
    if q:
        usuarios = db.execute(
            "SELECT * FROM users WHERE username LIKE ? OR email LIKE ?",
            (f"%{q}%", f"%{q}%")
        ).fetchall()
    else:
        usuarios = db.execute('SELECT * FROM users').fetchall()
    return render_template('admin_usuarios.html', usuarios=usuarios)

@main.route('/admin/juegos')
@admin_required
def admin_juegos():
    db = get_db()
    juegos = db.execute('SELECT * FROM games').fetchall()
    return render_template('admin_juegos.html', juegos=juegos)

# Crear juego
@main.route('/admin/juegos/crear', methods=['GET', 'POST'])
@admin_required
def crear_juego():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        db = get_db()
        db.execute('INSERT INTO games (name, description) VALUES (?, ?)', (nombre, descripcion))
        db.commit()
        flash('Juego creado correctamente.', 'success')
        return redirect(url_for('main.admin_juegos'))
    return render_template('crear_juego.html')

# Editar juego
@main.route('/admin/juegos/editar/<int:juego_id>', methods=['GET', 'POST'])
@admin_required
def editar_juego(juego_id):
    db = get_db()
    juego = db.execute('SELECT * FROM games WHERE id = ?', (juego_id,)).fetchone()
    if not juego:
        flash('Juego no encontrado.', 'danger')
        return redirect(url_for('main.admin_juegos'))
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        db.execute('UPDATE games SET name = ?, description = ? WHERE id = ?', (nombre, descripcion, juego_id))
        db.commit()
        flash('Juego actualizado.', 'success')
        return redirect(url_for('main.admin_juegos'))
    return render_template('editar_juego.html', juego=juego)

# Eliminar juego
@main.route('/admin/juegos/eliminar/<int:juego_id>', methods=['POST'])
@admin_required
def eliminar_juego(juego_id):
    db = get_db()
    db.execute('DELETE FROM games WHERE id = ?', (juego_id,))
    db.commit()
    flash('Juego eliminado.', 'success')
    return redirect(url_for('main.admin_juegos'))

# Editar usuario
@main.route('/admin/usuarios/editar/<int:user_id>', methods=['GET', 'POST'])
@admin_required
def editar_usuario(user_id):
    db = get_db()
    usuario = db.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    if not usuario:
        flash('Usuario no encontrado.', 'danger')
        return redirect(url_for('main.admin_usuarios'))
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        role = request.form['role']
        db.execute('UPDATE users SET email = ?, username = ?, role = ? WHERE id = ?', (email, username, role, user_id))
        db.commit()
        flash('Usuario actualizado.', 'success')
        return redirect(url_for('main.admin_usuarios'))
    return render_template('editar_usuario.html', usuario=usuario)

# Eliminar usuario
@main.route('/admin/usuarios/eliminar/<int:user_id>', methods=['POST'])
@admin_required
def eliminar_usuario(user_id):
    db = get_db()
    db.execute('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()
    flash('Usuario eliminado.', 'success')
    return redirect(url_for('main.admin_usuarios'))

# Crear usuario
@main.route('/admin/usuarios/crear', methods=['GET', 'POST'])
@admin_required
def crear_usuario():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']

        db = get_db()
        # Verificar si el correo o el nombre de usuario ya existen
        usuario_existente = db.execute(
            'SELECT id FROM users WHERE email = ? OR username = ?',
            (email, username)
        ).fetchone()

        if usuario_existente:
            flash('El correo o el nombre de usuario ya están registrados.', 'danger')
            return redirect(url_for('main.crear_usuario'))

        # Insertar el nuevo usuario en la base de datos
        db.execute(
            'INSERT INTO users (email, username, password, role) VALUES (?, ?, ?, ?)',
            (email, username, password, role)
        )
        db.commit()
        flash('Usuario creado correctamente.', 'success')
        return redirect(url_for('main.admin_usuarios'))

    return render_template('crear_usuario.html')

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

    # Datos para Chart.js
    ranking_puntos_labels = [r['username'] for r in ranking_puntos]
    ranking_puntos_data = [r['max_score'] for r in ranking_puntos]
    ranking_tiempo_labels = [r['username'] for r in ranking_tiempo]
    ranking_tiempo_data = [r['min_time'] for r in ranking_tiempo]

    return render_template(
        'dashboard.html',
        games=games,
        stats=stats,
        ranking_puntos=ranking_puntos,
        ranking_tiempo=ranking_tiempo,
        ranking_puntos_labels=ranking_puntos_labels,
        ranking_puntos_data=ranking_puntos_data,
        ranking_tiempo_labels=ranking_tiempo_labels,
        ranking_tiempo_data=ranking_tiempo_data
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