from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Hello from VM 3!"})  # Use jsonify()

if __name__ == '__main__':
    app.run(host='192.168.31.18', port=5003, debug=True)
