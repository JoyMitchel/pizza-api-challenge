# pizza-api-challenge

# 🍕 Pizza Restaurant API Challenge

A API built using Flask that allows clients to interact with data about pizza restaurants and the pizzas they offer. This project uses the MVC architecture with Flask, SQLAlchemy, and Flask-Migrate. No frontend is required — the API is tested using Postman.

---

## 🚀 Features

- View all restaurants and pizzas
- View a single restaurant with all pizzas it offers
- Add new restaurant-pizza associations with validations
- Delete a restaurant and cascade associated data
- Built using Flask, Flask-Migrate, SQLAlchemy, and SQLite
- Clean MVC structure

---

## 🧱 Project Structure

├── server/
│ ├── init.py
│ ├── app.py # App setup
│ ├── config.py # DB config
│ ├── seed.py # Data seeding script
│ ├── models/ # SQLAlchemy models
│ │ ├── init.py
│ │ ├── restaurant.py
│ │ ├── pizza.py
│ │ └── restaurant_pizza.py
│ ├── controllers/ # Route handlers
│ │ ├── init.py
│ │ ├── restaurant_controller.py
│ │ ├── pizza_controller.py
│ │ └── restaurant_pizza_controller.py
├── migrations/ # Flask-Migrate directory
├── challenge-1-pizzas.postman_collection.json
└── README.md


---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pizza-api-challenge.git
cd pizza-api-challenge
code . in terminal




