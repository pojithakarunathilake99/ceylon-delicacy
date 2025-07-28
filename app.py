import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "default-secret-key-for-development")

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/css/<path:filename>')
def css_files(filename):
    return send_from_directory('css', filename)

@app.route('/js/<path:filename>')
def js_files(filename):
    return send_from_directory('js', filename)

@app.route('/assets/<path:filename>')
def assets_files(filename):
    return send_from_directory('assets', filename)

@app.route('/attached_assets/<path:filename>')
def attached_assets_files(filename):
    return send_from_directory('attached_assets', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)