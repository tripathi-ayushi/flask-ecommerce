# 🛍️ My Flask eCommerce Journey

This project began as a personal challenge — turning everything I’d learned from building a simple blog in Flask into something more powerful, practical, and real-world: **an eCommerce site.**

I wanted more than static pages. I wanted:
- Users to register and log in securely 🔐
- Products to be listed and browsed 🛒
- A working cart system with real payment integration 💳

So I opened VS Code, made a folder named `flask-ecommerce`, and got started.

---

## ✨ What I Built

- ✅ A modular Flask app with Blueprints and factory pattern
- ✅ Secure login & registration with `Flask-Login` + hashed passwords
- ✅ Clean form handling using `Flask-WTF`
- ✅ SQLite + SQLAlchemy models
- ✅ A shopping cart (session-based)
- 🔄 Real payment integration with Stripe (in progress)
- 🔧 Responsive HTML (Bootstrap coming soon!)

This wasn’t just another CRUD app. I integrated real tools used in production-level apps — and learned a lot along the way.

---

## ⚙️ Technologies Used

- Python 3.12 🐍
- Flask (with Blueprints + App Factory Pattern)
- SQLAlchemy ORM + SQLite
- Flask-Login for session handling
- Flask-WTF for form validation
- Stripe Checkout API (for real payments)
- HTML + Jinja2 Templating
- Bootstrap (coming soon!)

---

## 📁 Project Structure

```
flask-ecommerce/
├── app/
│   ├── __init__.py          # App factory
│   ├── models.py            # SQLAlchemy models
│   ├── routes.py            # Views (register, login, home)
│   ├── forms.py             # Flask-WTF forms
│   ├── templates/           # Jinja2 HTML templates
│   └── static/              # CSS / JS / images
├── instance/                # Holds site.db
├── run.py                   # Main entry point
├── requirements.txt         # Python packages
└── README.md                # You’re reading it!
```

---

## 🧪 How to Run Locally

Clone the repo and run it in your local environment:

```bash
git clone https://github.com/tripathi-ayushi/flask-ecommerce.git
cd flask-ecommerce
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Visit `http://127.0.0.1:5000` in your browser 🚀

---

## 🔍 What I Learned

- Why Flask Blueprints are essential for scalable apps
- How to manage user sessions and secure passwords with Flask-Login
- How to validate forms without writing repetitive code
- How Stripe Checkout works — and how to safely handle payments
- How to structure real-world Flask projects beyond "hello world"

---

## 🚧 What's Next?

- Add admin panel for adding/removing products
- Build a cart and order history feature
- Add Stripe Checkout flow with webhook support
- Add Bootstrap for cleaner UI/UX
- Deploy to Render/Heroku

---

## 💡 Final Thoughts

This project taught me more about web dev than any tutorial ever could. I hit errors, broke things, fixed them — and finally got it working.

It’s still a work in progress, but now I have a real Flask-based eCommerce system I can proudly share.

---

Made with 💻 + ❤️ by [@tripathi-ayushi](https://github.com/tripathi-ayushi)
