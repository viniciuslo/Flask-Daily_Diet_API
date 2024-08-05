from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from . import routes, models
        app.register_blueprint(routes.bp)
        db.create_all()

    # Configurar Swagger
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Daily Diet API"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # Rota para servir o arquivo swagger.yaml
    @app.route('/static/<path:filename>')
    def static_files(filename):
        return send_from_directory(app.static_folder, filename)

    # Rota de teste para verificar se os arquivos estáticos estão sendo servidos
    @app.route('/test-static')
    def test_static():
        return send_from_directory(app.static_folder, 'swagger.yaml')

    return app
