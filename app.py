from flask import Flask, render_template, request, redirect, url_for
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    name = request.form.get('name')
    email = request.form.get('email')

    # Simulate storing subscription details (e.g., save to a database)
    print(f"New subscription: {name}, {email}")

    return redirect(url_for('index'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if no PORT variable is set
    app.run(host='0.0.0.0', port=port)



