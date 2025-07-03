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