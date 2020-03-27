from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def test():
    return '<h1>TEST</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
