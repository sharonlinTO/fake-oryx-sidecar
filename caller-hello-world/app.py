from flask import Flask
import os
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = requests.get("http://flask:5000")
    if response.ok:
        return response.content
    else:
        return "Response not found. Hi Sharon!"

@app.route('/goodbye')
def goodbye_world():
    response = requests.get("http://flask:5000/goodbye")
    if response.ok:
        return response.content
    else:
        return "Response not found. Bye Sharon!"

@app.route('/buildGo')
def build_go():
    response = requests.get("http://flask:5000/compileGo/main.go")
    if response.ok:
        return response.content
    else:
        return "Response not found. Compilation failed."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5324))
    app.run(debug=True, host='0.0.0.0', port=port)