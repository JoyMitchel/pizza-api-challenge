from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db

app = Flask(__name__)  # ✅ Only one instance

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Routes
@app.route('/')
def index():
    return "Hello, World!"                 

@app.route('/about')
def about():
    return "This is about us page"

@app.route('/<username>')
def username(username):
    return f'Hello {username}'

@app.route('/posts')

# Run the app manually for debugging
if __name__ == '__main__':
    app.run(debug=True, port=4000)


