# vm3_greeting_service.py
from flask import Flask

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return {"message": "Hello from VM 3!"}

if __name__ == '__main__':
    app.run(host='192.168.32.202', port=5003)
