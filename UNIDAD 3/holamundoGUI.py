from= Flask import Flask 

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "<h1>Hola Mundo desde Flask!</h1>"
