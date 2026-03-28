# SOC Defense API

from flask import Flask, request, jsonify
from core.analyzer import analyze_log
from core.response_engine import generate_response

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    log = data.get("log")

    # Analyze threat
    threat = analyze_log(log)

    # Generate defensive response
    response = generate_response(threat)

    return jsonify({
        "log": log,
        "threat": threat,
        "response": response
    })

# Run server
if __name__ == "__main__":
    app.run(debug=True)
