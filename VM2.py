
from flask import Flask
import random

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def get_random_number():
    random_number = random.randint(1, 100)
    return {"random_number": random_number}

if __name__ == '__main__':
    app.run(host='192.168.31.202', port=5002)
