from flask import Flask, request, jsonify

app = Flask('app')

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/ret', methods=['POST'])
def ret():
    json = request.json
    x = json['x']
    print(x)
    return jsonify({'x': x})

@app.route('/1')
def index1():
    return 'Hello universe!'



if __name__ == '__main__':
    app.run()