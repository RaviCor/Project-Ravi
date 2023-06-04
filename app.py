from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    db.init_app(app)

    from models import user

    with app.app_context():
        inspector = db.inspect(db.engine)
        existing_tables = inspector.get_table_names()
        check_tables = all(table in existing_tables for table in db.metadata.tables.keys())
        print(check_tables)
        if not check_tables:
            print("Creando tablas")
            db.create_all()

    @app.route('/')
    def index():
        return render_template("index.html")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

