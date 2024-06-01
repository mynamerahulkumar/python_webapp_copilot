from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    result = data['a'] + data['b']
    return {'result': result}

if __name__ == '__main__':
    app.run(port=5000)