from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RUNPOD_URL = "http://TON_ENDPOINT_RUNPOD/v1/chat"  # plus tard

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt", "")

    # pour test sans model
    return jsonify({
        "response": f"AurX (Render): {prompt}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
