from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_wolrd():
    return "¡Hola mundo!"

if __name__ == "__main__":
    app.run(debug=True)