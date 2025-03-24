from flask import Blueprint, render_template, redirect, url_for, flash
from app.forms import RegisterForm
from app import db
from app.models import User
from werkzeug.security import generate_password_hash
from flask_login import login_user
import requests  # use public APIs

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

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

@main.route('/store')
def store():
    response = requests.get("https://fakestoreapi.com/products")
    products = response.json()
    return render_template("store.html", products=products)

@main.route('/cart')
def cart():
    return render_template('cart.html')

@main.route('/checkout-success')
def checkout_success():
    return render_template('checkout_success.html')



