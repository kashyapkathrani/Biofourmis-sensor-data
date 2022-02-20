import json
from flask import Flask, request, abort, jsonify
import processor

app = Flask(__name__)

@app.route("/vitals_input", methods=['POST'])
def vitals_input():
    data = json.loads(request.data)
    print(data, type(data))

    processor.store_in_csv(data)

    return jsonify(message="Successfully added the data."), 201

@app.route("/vitals_output", methods=['GET'])
def vitals_output():
    interval = int(request.args.get("interval"))

    data = processor.get_report(interval)

    return jsonify(report=data), 200


@app.before_request
def validate_request():
    if request.endpoint == 'vitals_input':
        data = json.loads(request.data)
        required_fields = ['user_id', 'timestamp', 'heart_rate', 'respiration_rate', 'activity']

        for field in required_fields:
            if field not in data:
                abort(400, f"Missing required field - {field} in the request.")

    elif request.endpoint == 'vitals_output':
        interval = int(request.args.get("interval"))

        if interval < 15:
            abort(400, "Interval should be greater than 15 minutes")

if __name__ == "__main__":
    app.run(debug=True)
