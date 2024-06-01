from flask import Flask, request

app = Flask(__name__)

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = data['a'] - data['b']
    return {'result': result}

if __name__ == '__main__':
    app.run(port=5001)