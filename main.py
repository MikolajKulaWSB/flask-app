from flask import Flask, request, jsonify

app = Flask('app')

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/2')
def index2():
    return 'Hi there, Jakub here!'

@app.route('/ret', methods=['POST'])
def ret():
    json = request.json
    x = json['x']
    print(x)
    return jsonify({'x': x})

if __name__ == '__main__':
    app.run()