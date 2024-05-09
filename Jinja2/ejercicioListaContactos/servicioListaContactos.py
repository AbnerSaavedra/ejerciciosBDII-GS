from flask import Flask, render_template, request, jsonify, redirect, url_for, flash

app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = 'clave secreta'

contactsList = []

@app.route("/list", methods=["GET"])
def list():
    return render_template("lista.html.jinja", contactsList=contactsList)

@app.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        email = request.form['email']
        direccion = request.form['direccion']

        if not nombre:
            flash("El nombre es obligatorio")
        
        if not apellido:
            flash("El apellido es obligatorio")

        if not telefono:
            flash("El teléfono es obligatorio")

        if not email:
            flash("El email es obligatorio")

        if not direccion:
            flash("La dirección es obligatorio")

        if nombre and apellido and telefono and email and direccion:
            contactsList.append({'nombre': nombre, 'apellido': apellido, 'telefono': telefono, 'email': email, 'direccion': direccion})
            return redirect(url_for('list'))

    return render_template('formContacto.html.jinja')

@app.route("/contactDetail/<int:index>")
def contactDetail(index):
    contacto = contactsList[index]
    return render_template('detalleContacto.html.jinja', contacto=contacto)

if __name__ == "__main__":
    app.run(debug=True)