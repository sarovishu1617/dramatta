<<<<<<< HEAD
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Step 1: Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Step 2: Initialize SQLAlchemy
db = SQLAlchemy(app)

# Step 3: Create User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(20), nullable=False)

# Step 4: Create the database
with app.app_context():
    db.create_all()

# Step 5: Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['Password']  # Match name in HTML

        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return render_template('home.html', email=user.email)
        else:
            return "Invalid email or password"

    return render_template('login.html')

# Step 6: Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        number = request.form['number']

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "User already exists!"

        new_user = User(name=name, email=email, password=password, number=number)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html')

# Step 7: Run the app
=======
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user for testing
users = {
    "test@example.com": "1234",  # email: password
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Authentication logic
        if email in users and users[email] == password:
            return render_template('success.html', email=email)
        else:
            error = "Invalid email or password"
            return render_template('login.html', error=error)

    return render_template('login.html')

>>>>>>> e57f2f12682a76bbbe5fa33253e8e50340e31cd2
if __name__ == '__main__':
    app.run(debug=True)
