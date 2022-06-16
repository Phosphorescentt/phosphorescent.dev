from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Docker & GitHub actions test!</h1><br><h4>Testing Docker and GitHub actions!</h4>"


if __name__ == "__main__":
    app.run(debug=True)
