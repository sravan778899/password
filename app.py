from flask import Flask, render_template, request

app = Flask(__name__)

def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password):
        score += 1

    if score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    else:
        return "Weak"

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    if request.method == 'POST':
        password = request.form['password']
        strength = check_strength(password)
    return render_template('index.html', strength=strength)

if __name__ == '__main__':
    app.run(debug=True)
