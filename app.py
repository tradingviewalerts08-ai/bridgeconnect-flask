from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Store signals per client ID
client_signals = {}

@app.route('/signal/<client_id>', methods=['POST'])
def receive_signal(client_id):
    data = request.get_json()
    if data:
        client_signals[client_id] = data
        print(f"Signal received for client {client_id}: {data}")
        return jsonify({"status": "ok"}), 200
    return jsonify({"status": "error"}), 400

@app.route('/signal/<client_id>', methods=['GET'])
def get_signal(client_id):
    signal = client_signals.get(client_id)
    if not signal:
        return jsonify({}), 200
    client_signals[client_id] = {}
    print(f"Signal served and cleared for client {client_id}: {signal}")
    return jsonify(signal), 200

@app.route('/', methods=['GET'])
def home():
    return "BridgeConnect Universal Flask Running", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
