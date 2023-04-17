from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur mon mini site web !"
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur mon mini site web toto!"

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(debug=True)