from flask import Flask
from flask_bycrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'main.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object('config_class')
    
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)

    from App import routes, models

    app.register_blueprint(routes.bp)

    @app.context_processor
    def utility_processor():
        return dict(enumerate=enumerate)
    
    return app


