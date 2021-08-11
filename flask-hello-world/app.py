from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/goodbye')
def goodbye_world():
    return 'Goodbye, world!'

@app.route('/compileGo/<fileLoc>')
def compile_go(fileLoc):
    if not os.path.isfile(fileLoc):
        return 'File not found.'

    subprocess.run(["go", "build", fileLoc])

    return 'Complete!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)