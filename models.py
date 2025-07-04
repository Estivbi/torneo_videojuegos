import email
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def get_db():
    conn = sqlite3.connect('instance/usuarios.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_user_table():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0
        )
    ''')
    db.commit()

def add_user(username, password, is_admin=0):
    db = get_db()
    db.execute(
        'INSERT INTO users (email, username, password, is_admin) VALUES (?, ?, ?, ?)',
        (email, username, generate_password_hash(password), is_admin)
    )
    db.commit()

def get_user(username):
    db = get_db()
    return db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()


def get_user_by_email(email):
    db = get_db()
    return db.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()

def get_user_by_credentials(username, password):
    db = get_db()
    user = db.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    if user and user['password'] == password:
        return user
    return None

# --- Tablas de juegos y partidas ---

def create_game_table():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )
    ''')
    db.commit()

def create_match_table():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            game_id INTEGER NOT NULL CHECK(game_id IN (1, 2)),
            level TEXT CHECK(level IN ('amateur', 'normal', 'expert')) NOT NULL,
            score INTEGER DEFAULT 0,
            time INTEGER DEFAULT 0,
            result TEXT CHECK(result IN ('Victoria', 'Derrota', 'Empate')) DEFAULT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(game_id) REFERENCES games(id)
        )
    ''')
    db.commit()

def insert_default_games():
    db = get_db()
    count = db.execute('SELECT COUNT(*) as c FROM games').fetchone()['c']
    if count == 0:
        db.execute(
            "INSERT INTO games (id, name, description) VALUES (?, ?, ?)",
            (1, 'Speed Run', 'Gana el que complete el nivel en el menor tiempo posible.')
        )
        db.execute(
            "INSERT INTO games (id, name, description) VALUES (?, ?, ?)",
            (2, 'High Score', 'Gana el que obtenga la mayor puntuación.')
        )
        db.commit()