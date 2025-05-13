from flask import Flask, request, jsonify

app = Flask(__name__)
messages = []

@app.route('/message', methods=['POST'])
def send_message():
    data = request.json
    messages.append(data['message'])
    return jsonify({"status": "Mensagem recebida!"}), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages), 200

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.json
    result = data['a'] + data['b']
    return jsonify({"resultado": result}), 200

if __name__ == '__main__':
    app.run(debug=True)