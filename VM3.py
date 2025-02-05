VM 3: Greeting Service  

This microservice will return a greeting message. 

# vm3_greeting_service.py
from flask import Flask

app = Flask(_name_)

@app.route('/greet', methods=['GET'])
def greet():
    return {"message": "Hello from VM 3!"}

if _name_ == '_main_':
    app.run(host='192.168.32.18', port=5003)

