from flask import Flask

app = Flask(__name__)

@app.route("/")
def la_funcion():
    return "Hola, Mundo!"

