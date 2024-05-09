from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__, template_folder="./templates")

messagesList = []

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        messagesList.append({'title': title, 'content': content})
        return redirect(url_for('messages'))

    return render_template('contact.html.jinja')

@app.route("/messages")
def messages():
    return render_template('messages.html.jinja', messages=messagesList)

if __name__ == "__main__":
    app.run(debug=True)