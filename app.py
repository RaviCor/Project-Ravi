from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Directorio base de la aplicación
basedir = os.path.abspath(os.path.dirname(__file__))

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Crear la instancia de la base de datos
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Crear un usuario de ejemplo
with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        user = User(username='admin', password=generate_password_hash('admin123'))
        db.session.add(user)
        db.session.commit()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Buscar el usuario en la base de datos
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            return redirect(url_for('tasks'))
        else:
            return render_template('login.html', error=True)

    return render_template('login.html', error=False)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/tasks')
def tasks():
    return render_template('tasks.html')

@app.route('/forgot-password')
def forgot_password():
    return 'Página de restablecimiento de contraseña'

if __name__ == '__main__':
    app.run()
