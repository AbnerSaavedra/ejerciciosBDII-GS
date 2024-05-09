from flask import Flask, request

app = Flask(__name__)

@app.route("/nombre", methods=["GET"])
def get_request():
    return "Hola nombre"

@app.route("/saludar/<nombre>", methods=["GET"])
def saludar(nombre):
    return f"¡Hola, {nombre}!"

@app.route("/despedir", methods=["GET"])
def despedir():
    name = request.args.get("name")
    if name != None:
        return f"¡Adiós, {name}!"
    else:
        return "Adiós"
    
@app.route("/message", methods=["GET", "POST"])
def message():

    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        return '''
            <h1>The name value is: {}</h1>
            <h1>The mesage value is: {}</h1>
            '''.format(name, message)
    
    return '''
            <form method="POST">
            <div><label>Name: <input type="text" name="name"></label></div>
            <div><label>Message: <input type="text" name="message"></label></div>
            <input type="submit" value="Submit">
            </form>'''
        #f"Hola {name} tu mensaje es : {message}"

if __name__ == "__main__":
    app.run(debug=True)