from flask import Flask
from routes.main import main as main_blueprint
from routes.auth import auth as auth_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config.from_pyfile('instance/config.py', silent=True)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)