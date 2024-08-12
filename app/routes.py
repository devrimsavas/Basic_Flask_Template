
from flask import Blueprint,render_template, jsonify,request

main=Blueprint('main',__name__)

@main.route('/')
def index():
    title="Home Page of Flask Template"

    return render_template('index.html',title=title)

@main.route('/staff') 
def staff():
    title="Staff Page of Flask Template"

    return render_template('staff.html',title=title)

@main.route('/newstaffrecord', methods=["POST"])
def newstaffrecord():
    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    position = request.form.get("position")

    if not name or not age or not gender or not position:
        return jsonify({"error": "All fields are required"}), 400

    person = {
        "name": name,
        "age": age,
        "gender": gender,
        "position": position
    }

    print("Person added is ----- :", person)

    return jsonify(person)