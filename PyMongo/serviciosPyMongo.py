from flask import Flask, request, render_template, redirect, url_for, flash
from db import collection
from bson.objectid import ObjectId

app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "clave secreta"

listaElementos = []

@app.route("/list", methods=["GET"])
def getList():
    listaElementos = collection.find()

    return render_template('lista.html.jinja', listaElementos=listaElementos)

@app.route('/', methods=['GET', 'POST'])
def add_element():
    if request.method == "POST":
        nombre = request.form['nombre']
        edad = request.form['edad']
        #form = request.get_json()
        object = {
            'nombre': nombre,
            'edad': edad
        }
        collection.insert_one(object)
    return render_template("contact.html.jinja")

@app.route('/<id>', methods=['GET'])
def get_element(id):
    oid = ObjectId(id)
    element = collection.find_one({'_id', oid})
    #return render_template(..., element = element)

@app.route('/update/<id>', methods=['GET', 'POST'])
def update_element():
    if request.method == "POST":
        oid = ObjectId(id)
        new_element = request.form
        element = collection.replace_one({'_id': id}, 
                                         {'nombre': new_element['nombre'],
                                          'edad': new_element['edad']})
        #return render_template()

@app.route('/delete/<id>', methods=['POST'])
def delete_element(id):
    oid = ObjectId(id)
    element = collection.delete_one({'_id': oid})
    #return render_template()

if __name__ == "__main__":
    app.run(debug=True)


