from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_block', methods=['POST'])
def add_block():
    namespace = request.form['namespace']
    data = request.form['data']
    command = f"python3 add_block.py --namespace {namespace} --data {data}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    output = stdout.decode('utf-8') if stdout else stderr.decode('utf-8')
    return output, 200 if process.returncode == 0 else 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
