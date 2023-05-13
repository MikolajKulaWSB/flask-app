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

@app.route('/1')
def index1():
    return 'Hello universe!'


@app.route('/endpoint/aga')
def hello():
    return "Uszanowanko, WOW!"

@app.route('/endpoint/marta')
def hello2():
    return "Pyton! :)"

@app.route("/endpoint/ola")
def hello3():
    return "Gdzie jest drwal??"


if __name__ == '__main__':
    app.run()