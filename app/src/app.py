from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'message': 'Linux Infrastructure CI/CD App',
        'status': 'running'
    })

@app.route('/healthz')
def healthz():
    return jsonify({
        'status': 'ok',
        'timestamp': time.time()
    }), 200

@app.route('/ready')
def ready():
    return jsonify({
        'status': 'ready'
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
