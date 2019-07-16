from flask import Flask
from flask import json
from flask import request
from flask import Response
import mysql.connector

app = Flask(__name__)
config = {
  'user': 'root',
  'password': 'BeReSeMi.DataScience',
  'host': 'database',
  'database': 'data_science',
  'raise_on_warnings': False
}

@app.route('/', methods=['GET'])
def index():     
    content = open("index.html").read()
    return Response(content, mimetype="text/html")

@app.route('/employees', methods = ["POST"])
def addEmployee():
    print("Request: " + json.dumps(request.json))
    
    data_json = json.loads(request.data)
    name = data_json['name']
    hobbies = data_json['hobbies']
    role = data_json['role']

    add_employee = ("INSERT INTO employees (name, hobbies, role) VALUES (%s, %s, %s)")

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    cursor.execute(add_employee, (name, hobbies, role))
    emp_no = cursor.lastrowid

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()

    data = {
        "emp_no": emp_no
    }    
    js = json.dumps(data)

    return Response(js, status=200, mimetype='application/json')

@app.route('/employees', methods = ["GET"])
def getEmployees():

    query = ("SELECT name, hobbies, role FROM employees")

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    cursor.execute(query)

    data = []
    for (name, hobbies, role) in cursor:
      data.append({"name": name, "hobbies": hobbies, "role": role})

    cursor.close()
    cnx.close()

    js = json.dumps(data)
    return Response(js, status=200, mimetype='application/json')

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=8787)