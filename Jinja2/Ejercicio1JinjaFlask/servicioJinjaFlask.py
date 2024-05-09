from flask import Flask, render_template, request, jsonify

listaTareas = []
app = Flask(__name__, template_folder="./templates")

@app.route("/agregarTareas", methods=["GET", "POST"])
def agregarTarea():
    mensaje = ""
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")

        if name != "Jugar":
            listaTareas.append({"name": name, "description": description})
        else:
            mensaje = "Tarea no permitida"
            #return jsonify({"errores": "Invalid request"}), 400
    return render_template("agregarTareas.html.jinja", listaTareas=listaTareas, mensaje= mensaje)

if __name__ == "__main__":
    app.run(debug=True)