from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    print("✅ Inside create_app()")

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'  # Replace with env var in production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)

    # Set login view for @login_required
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # Import blueprints and register them
    from .routes import main
    app.register_blueprint(main)

    # You can register auth blueprint later like:
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)

    return app

# User loader for Flask-Login
from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

