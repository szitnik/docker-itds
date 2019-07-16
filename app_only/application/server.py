from flask import Flask
from flask import json
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():     
    content = open("index.html").read()
    return Response(content, mimetype="text/html")

if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=8787)