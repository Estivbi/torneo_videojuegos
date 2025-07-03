# crea_db.py
from models import create_user_table

if __name__ == '__main__':
    create_user_table()
    print("Base de datos y tabla de usuarios creadas.")