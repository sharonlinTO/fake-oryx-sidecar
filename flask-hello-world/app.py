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

@app.route('/compileGo/<fileName>')
def compile_go(fileName):

    # Specify the file path
    fileLoc = os.path.join("/data", fileName)

    # Make sure that the file exists at the location
    if not os.path.isfile(fileLoc):
        return f'File not found. File specified: {fileLoc}'

    if not fileName.endswith(".go"):
        return f'Not a go file. File specified: {fileName}'

    # Get the parent directory
    fileDir = os.path.dirname(fileLoc)

    # TODO: Mount in docker volume
    subprocess.run(["go", "build", "-o", fileDir, fileLoc])

    return f'Complete! Binary is in: {fileDir}'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)