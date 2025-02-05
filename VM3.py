from flask import Flask

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return {"message": "Hello from VM 3!"}

if __name__ == '__main__':
    # Use '0.0.0.0' to bind the app to all available network interfaces
    # or use the actual local IP if you prefer
    app.run(host='192.168.31.202', port=5003)
