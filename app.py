from flask import Flask, Response, request
import os
import subprocess

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def send_success():
    return Response('I am fake Oryx :)', 200)

# NOTE: file must be called main.go
@app.route('/build', methods = ['POST'])
def compile_go():

    # Only accept POST requests
    if request.method != "POST":
        return Response(f'Only POST requests are supported. {request.form} ', 405)
    
    # Only support Golang for now
    platform = request.form.get("platform")
    if platform != "go":
        return Response(f'Only Go platform is supported at this time. Submitted platform: {request.form}', 400)

    # File should be in repository folder
    fileLoc = "/home/site/repository/main.go"
    if not os.path.isfile(fileLoc):
        return Response(f'File not found. Looking for: {fileLoc} {request.form} ', 404)

    # Place file in /home/site/wwwroot/
    returnCode = subprocess.call(["go", "build", "-o", "/home/site/wwwroot/main", fileLoc], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if returnCode == 0:
        return Response(f'Build complete. Binary located in /home/site/wwwroot/ {request.form} ', 200)
    else:
        return Response(f'Build Failed. {request.form} ', 400)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)