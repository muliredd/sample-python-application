from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Python app in Kubernetes!",
        "environment": os.getenv("APP_ENV", "development")
    })

if __name__ == "__main__":
    # Run on all interfaces for Kubernetes
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
