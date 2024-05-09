import random
from flask import Flask, request, jsonify

app = Flask(__name__)

student_names = ["John", "Jane", "Bob", "Alice", "Mike", "Emma", "Oliver", "Sophia"]
notes = [random.randint(0, 100) for _ in range(10)]

@app.route('/materia', methods=["GET"])
def get_students():
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

    return jsonify({"materia": nombre, "estudiantes": students})

if __name__ == "__main__":
    app.run(debug=True)