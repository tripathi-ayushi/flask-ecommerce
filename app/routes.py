from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import RegisterForm
from app import db
from app.models import User
from werkzeug.security import generate_password_hash
from flask_login import login_user

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "<h1>Welcome to the Flask eCommerce Site</h1>"

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if user already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please log in.', 'warning')
            return redirect(url_for('main.register'))

        # Hash password and save new user
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)  # Automatically log in after register
        flash('Account created successfully!', 'success')
        return redirect(url_for('main.home'))

    return render_template('register.html', form=form)
