from flask import Flask, request, jsonify

app = Flask('app')

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/23')
def index23():
    return 'Hello WSB'

@app.route('/ret', methods=['POST'])
def ret():
    json = request.json
    x = json['x']
    print(x)
    return jsonify({'x': x})

if __name__ == '__main__':
    app.run()