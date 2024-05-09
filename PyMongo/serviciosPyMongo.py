from flask import Flask, request, render_template, redirect, url_for, flash
from db import collection
from bson.objectid import ObjectId

app = Flask(__name__, template_folder="./templates")
app.config['SECRET_KEY'] = "clave secreta"

elementsList = []

@app.route("/list", methods=["GET"])
def getList():
    elementsList = collection.find()

    return render_template('lista.html.jinja', elementsList=elementsList)

@app.route('/', methods=['GET', 'POST'])
def add_element():
    if request.method == "POST":
        nombre = request.form['nombre']
        edad = request.form['edad']
        object = {
            'nombre': nombre,
            'edad': edad
        }
        collection.insert_one(object)
        return redirect(url_for('getList'))
    return render_template("add.html.jinja")

@app.route('/<id>', methods=['GET'])
def get_element(id):
    oid = ObjectId(id)
    element = collection.find_one({'_id': oid})
    return render_template('detail.html.jinja', element = element)

@app.route('/update/<id>', methods=['GET', 'POST'])
def update_element(id):
    oid = ObjectId(id)
    element = collection.find_one({'_id': oid})
    if request.method == "POST":
        new_element = request.form
        collection.replace_one({'_id': oid}, 
                                         {'nombre': new_element['nombre'],
                                          'edad': new_element['edad']})    
        return redirect(url_for('getList'))
    return render_template("update.html.jinja", element=element)

@app.route('/delete/<id>', methods=['GET'])
def delete_element(id):
    oid = ObjectId(id)
    element = collection.delete_one({'_id': oid})
    return redirect(url_for('getList'))

if __name__ == "__main__":
    app.run(debug=True)


