import random
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder="./templates")

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

@app.route("/home/<saludo>", methods=["GET"])
def home(saludo):
    return render_template("home.html.jinja", saludo=saludo )

@app.route("/listar", methods=["GET"])
def listar():
    student_names = ["John", "Jane", "Bob", "Alice", "Mike", "Emma", "Oliver", "Sophia"]
    notes = [random.randint(0, 100) for _ in range(10)]
    nombre = request.args.get('nombre')
    cantidad_str = request.args.get('cantidad')

    if not nombre or not cantidad_str:
        return jsonify({"errores": "Invalid request"}), 400

    try:
        cantidad = int(cantidad_str)
    except ValueError:
        return jsonify({"error": "Cantidad debe ser un número entero"}), 400

    students = []
    for _ in range(cantidad):
        student_name = random.choice(student_names)
        note = random.choice(notes)
        approved = "Aprobó" if note >= 60 else "No aprobó"
        students.append({"nombre": student_name, "nota": note, "aprobado": approved})
    return render_template("listaEstudiantes.html.jinja", students=students )

@app.route("/verificarMayoriaEdad/<listaPersonas>", methods=['GET'])
def verificarMayoriaEdad(listaPersonas):

 listaPersonas = [{"nombre": "Daniel", "edad": 32}, {"nombre": "Omar", "edad": 55}, 
                  {"nombre": "Lino" , "edad": 20}, {"nombre": "Paula" , "edad": 17 },
                  {"nombre": "Sarah", "edad":15 }]
 return render_template("listaPersonas.html.jinja", listaPersonas
                        =listaPersonas)

if __name__ == "__main__":
    app.run(debug=True)