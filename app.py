from flask import Flask, Response, request
import os
import subprocess

app = Flask(__name__)

# NOTE: file must be called main.go
@app.route('/', methods = ['POST'])
def compile_go():

    # Only accept POST requests
    if request.method != "POST":
        return Response('Only POST requests are supported.', 405)
    
    # Only support Golang for now
    framework = request.form.get("framework")
    if framework != "GO":
        return Response(f'Only Go framework is supported at this time.', 400)

    # File should be in repository folder
    fileLoc = "/home/site/repository/main.go"
    if not os.path.isfile(fileLoc):
        return Response(f'File not found. Looking for: {fileLoc}', 404)

    # Place file in /home/site/wwwroot/
    returnCode = subprocess.call(["go", "build", "-o", "/home/site/wwwroot/main", fileLoc], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if returnCode == 0:
        return Response(f'Build complete. Binary located in /home/site/wwwroot/', 200)
    else:
        return Response('Build Failed.', 400)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)