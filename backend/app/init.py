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

if __name__ == '__main__':
    app.run(debug=True)
