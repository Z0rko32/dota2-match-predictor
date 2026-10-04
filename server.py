from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model("model.keras")
with open("scaler") as f:
    scaler = list(map(float, f.readline().split()))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict")
def predict():
    values = request.args.get("values")

    if not values:
        return jsonify({"error": "No values provided"}), 400
    try:
        numbers = list(map(float, values.split(",")))
    except ValueError:
        return jsonify({"error": "Invalid number format"}), 400
    if len(numbers) != 15:
        return jsonify({"error": "Exactly 15 numbers required"}), 400

    prediction = model.predict(np.array([[x / s for x, s in zip(numbers, scaler)]]))
    return jsonify({"prediction": float(prediction[0][0])})


if __name__ == "__main__":
    app.run(debug=True)
