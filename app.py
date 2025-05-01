# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiply', methods=['GET'])
def multiply():
    a = int(request.args.get('a', 1))
    b = int(request.args.get('b', 1))
    return jsonify({'result': a * b})

@app.route('/html', methods=['GET'])
def writehtml():
    index_page = '''<html><head><body><h2 align="center">Welcome to the page</body></head></html>'''
    return index_page

if __name__ == '__main__':
    app.run(debug=True)
