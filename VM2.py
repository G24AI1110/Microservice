VM 2: Random Number Service  

This microservice will return a random number between 1 and 100. 

# vm2_random_number_service.py
from flask import Flask
import random

app = Flask(_name_)

@app.route('/random', methods=['GET'])
def get_random_number():
    random_number = random.randint(1, 100)
    return {"random_number": random_number}

if _name_ == '_main_':
    app.run(host='192.168.31.202', port=5002)
