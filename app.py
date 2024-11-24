from flask import Flask, render_template, request
import requests


app = Flask(__name__)

def fetch_response(word):
    API_URL = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Something went wrong"}

@app.route("/", methods = ["GET", "POST"])
def index():
    response_data = None
    if request.method == "POST":
        word = request.form.get("word_input")
        response_data = fetch_response(word)

    return render_template("index.html", response_data = response_data)

if __name__ == "__main__":
    app.run(debug = True)