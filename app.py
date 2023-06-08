from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig, ProdConfig
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app(enviroment):
    app = Flask(__name__)
    
    if "DevConfig" in enviroment:
        app.config.from_object(DevConfig)
    elif "ProdConfig" in enviroment:
        app.config.from_object(ProdConfig)
    
    db.init_app(app)
    login_manager.init_app(app)

    from models.user import User

    with app.app_context():
        inspector = db.inspect(db.engine)
        existing_tables = inspector.get_table_names()
        check_tables = all(table in existing_tables for table in db.metadata.tables.keys())
        if not check_tables:
            print("Creando tablas para la base de datos.")
            db.create_all()

    @app.route('/')
    def index():
        return render_template("index.html")

    with app.app_context():
        from auth.auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix='/auth')

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)
    
    print(app.blueprints)

    return app

if __name__ == "__main__":
    app = create_app("DevConfig")  # Pasa la configuración como argumento
    app.run()
