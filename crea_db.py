# crea_db.py
from models import create_user_table, create_game_table, create_match_table, insert_default_games

if __name__ == '__main__':
    create_user_table()
    create_game_table()
    create_match_table()
    insert_default_games()
    print("Base de datos y todas las tablas creadas correctamente.")