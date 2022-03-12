from flask import Flask

app = Flask(__name__)

@app.route("/")
def la_funcion():
    return "Hola, Mundo!"

@app.route("/bye/<nombre>")
def otra_funcion(nombre):
    return f"hasta luego {nombre}"
    

