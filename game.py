from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

secret_number = random.randint(1, 100)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    global secret_number

    data = request.get_json()
    user_guess = int(data["guess"])

    if user_guess < secret_number:
        return jsonify({"result": "low"})
    elif user_guess > secret_number:
        return jsonify({"result": "high"})
    else:
        secret_number = random.randint(1, 100)
        return jsonify({"result": "correct"})

if __name__ == "__main__":
    app.run(debug=True)