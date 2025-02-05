vm1_time_service.py
from flask import Flask
from datetime import datetime

app = Flask(_name_)

@app.route('/time', methods=['GET'])
def get_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"current_time": current_time}

if _name_ == '_main_':
    app.run(host= '192.168.31.136', port=5001)
