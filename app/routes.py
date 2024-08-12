
from flask import Blueprint,render_template, jsonify,request
import boto3

from botocore.exceptions import NoCredentialsError,ClientError,PartialCredentialsError

main=Blueprint('main',__name__)

#initialise dynamodb
dynamodb=boto3.resource(
    'dynamodb',
    region_name='eu-north-1',
    aws_access_key_id='AKIATCKAS5YEAWWUO5AZ',
    aws_secret_access_key='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'
)

#referance to the table 
table=dynamodb.Table('StaffRecords')

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

    try: 
        table.put_item(Item=person)

        return jsonify(person)
    except (NoCredentialsError,PartialCredentialsError) as e:
        print(f"Credentials error: {e}")
        return jsonify({"error": "Credentials not configured correctly"}), 500
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An error occurred while adding the person to the database"}), 500