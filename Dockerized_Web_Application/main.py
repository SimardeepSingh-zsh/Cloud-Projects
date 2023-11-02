from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'  # Change to your database connection string
db = SQLAlchemy(app)

# Define a database model (an example)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

@app.route('/')
def home():
    return 'Welcome to the advanced Python web application!'

@app.route('/users')
def list_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username} for user in users]
    return jsonify(user_list)

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return f'User ID: {user.id}, Username: {user.username}'
    return 'User not found'

@app.route('/create_user', methods=['POST'])
def create_user():
    username = request.json.get('username')
    if username:
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        return f'User created with ID: {new_user.id}'
    return 'Invalid input'

if __name__ == '__main__':
    db.create_all()  # Initialize the database
    app.run(host='0.0.0.0', port=80)
