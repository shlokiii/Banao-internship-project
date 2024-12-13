from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # HTML template for your homepage

if __name__ == "__main__":
    # Use Render's $PORT environment variable or default to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)