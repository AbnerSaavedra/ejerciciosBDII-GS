from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="./templates")

@app.route("/tasks", methods=["GET"])
def tasks():

    listaTareas = [
        "Afeitarme la barba cada 2 días",
        "Montar las arepas",
        "Desayunar",
        "Alistarme", 
        "Ir a GracoSoft"
    ]
    return render_template("lista.html.jinja", listaTareas=listaTareas)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about_me.html.jinja')

if __name__ == "__main__":
    app.run(debug=True)