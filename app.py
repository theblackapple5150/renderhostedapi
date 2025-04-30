# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiply', methods=['GET'])
def multiply():
    a = int(request.args.get('a', 1))
    b = int(request.args.get('b', 1))
    return jsonify({'result': a * b})

if __name__ == '__main__':
    app.run(debug=True)
