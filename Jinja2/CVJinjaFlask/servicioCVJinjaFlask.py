from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder="./templatesJinja")

@app.route("/CV", methods=["GET"])
def CV():
    personalData = {"name": "Abner Saavedra", "address": "Lara"}
    workExperience = [{"title": "Fullstack developer (remote mode)", "factory": "Hispanos soluciones", "startDate": "October 2022", "endDate": "January 2023",
                       "activities":["NodeJS/Angular fullstack developer at Ragatex.",
"Data model creation and implementation",
"REST API service development",
"Integration and consumption of REST API services",
"Testing and debugging REST API services",
"Creation and integration of software components",
"Debugging and improvement of existing functionalities",
"HTML and CSS web layout",
"Continuous integration of advances",]}]

    return render_template("landing.html.jinja", personalData=personalData, workExperience=workExperience)

if __name__ == "__main__":
    app.run(debug=True)