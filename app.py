from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask Web App!</h1><p>This is running on a VM.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
