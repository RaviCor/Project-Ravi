from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user
from models.user import User 

auth = Blueprint('auth', __name__,
    template_folder='templates/',)
    #static_folder='static', static_url_path='auth')

# Ruta de inicio de sesión
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Buscar el usuario en la base de datos
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            # Iniciar sesión del usuario
            login_user(user)
            return redirect(url_for('auth.profile'))
        else:
            flash('Nombre de usuario o contraseña incorrectos', 'error')

    return render_template('login.html')

# Ruta de cierre de sesión
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Has cerrado sesión correctamente'

# Ruta protegida
@auth.route('/profile')
@login_required
def profile():
    return 'Perfil de usuario'

# Ruta de manejo de error de autenticación
#@login_manager.unauthorized_handler
#def unauthorized():
#    return 'Debes iniciar sesión para acceder a esta página', 401
