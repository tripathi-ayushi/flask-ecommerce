# 🛍 Flask eCommerce - From Scratch to Storefront

> 💻 "I was just trying to build a simple shopping cart...  
> Now I have a full eCommerce site, 3 terminal tabs open, 2 cups of chai, and 47 console logs saying 'undefined'."  
> — Every developer ever.

---

Hey there! 👋  
I'm Ayushi, and this is my journey of building a **full-stack eCommerce web app using Flask** — without using templates or starter kits.  
This project started as an experiment to level up my web development skills, and turned into a surprisingly complete shopping experience powered by Python, HTML, CSS, and JavaScript.

---

## ✅ What’s Working So Far

### 🛍 Product Store (Powered by a Public API)
- Pulled live mock data using [Fake Store API](https://fakestoreapi.com/)
- Displayed dynamic product listings with price, image, and description
- Styled the store using custom CSS

### 🛒 Add to Cart (With LocalStorage + JS)
- Added “Add to Cart” buttons for each product
- Cart stored in `localStorage` using vanilla JavaScript
- Live cart updates — no reload required

### 🧾 Cart Page
- View items added to cart
- Dynamic total price calculation
- “Remove” & “Clear Cart” buttons work instantly with JS

### ✅ Fake Checkout Flow
- “Place Order” button simulates a real checkout
- Redirects to a success page
- Automatically clears the cart (like a real transaction)

### 🏠 Homepage
- A clean landing page at `/`
- Navigation to store, cart, register, and login
- Lays foundation for a smooth user experience

---

## 🔧 Technologies Used

- **Python 3.12**
- **Flask** (with Blueprints and App Factory Pattern)
- **HTML, CSS, Jinja2 Templates**
- **JavaScript** (localStorage for cart logic)
- **Fake Store API** for product data  
- *(SQLAlchemy, Flask-Login, and Flask-WTF already integrated and ready for future features)*

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
│   └── static/
├── instance/                # Holds site.db
├── run.py                   # Main entry point
├── requirements.txt         # Python packages
└── README.md                # You’re reading it!
```

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/tripathi-ayushi/flask-ecommerce.git
cd flask-ecommerce
python -m venv venv
venv\Scripts\activate    # or source venv/bin/activate on Linux/Mac
pip install -r requirements.txt
flask run
```

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to start shopping!

---

## 🧠 What I’ve Learned So Far

- How to call external APIs and render live data in Flask  
- How to use JavaScript + localStorage for frontend cart logic  
- How to structure Flask apps with Blueprints and app factory  
- How routing, session, and templating all come together  
- How to break things… and how to fix them 😅  

---

## 📌 What’s Next?

Here’s what’s cooking for future commits:

- 🔗 Create a shared `base.html` layout with a navbar  
- 🔐 Use `@login_required` to protect `/cart` and `/checkout-success`  
- 🧾 Add an Order History page (save orders in a DB)  
- 🧑‍💼 Build an Admin Panel to manage products  
- 💅 Add Bootstrap or Tailwind for responsive styling  
- 🚀 Deploy to Render or Heroku  

---

## 💡 Why I'm Building This

This project is my deep dive into bringing **frontend + backend + real user flows** together — all from scratch, no shortcuts.

And let’s be real... eCommerce is one of the best ways to practice full-stack skills that actually apply to real-world jobs.

---

## 🙌 Final Thoughts

This isn’t just another CRUD project.  
It’s my playground — where I get to blend Flask with frontend logic, experiment with API data, and simulate real user flows like browsing, carting, and checking out.

More features are on the way. Until then — thanks for visiting!  

Made with 💻 + ❤️ by [@tripathi-ayushi](https://github.com/tripathi-ayushi)
