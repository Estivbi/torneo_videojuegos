from flask import Flask
from routes import main as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.config.from_pyfile('instance/config.py', silent=True)

    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)