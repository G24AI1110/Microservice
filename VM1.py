from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}

if __name__ == '__main__':
    app.run(host='192.168.145.79', port=5001)
