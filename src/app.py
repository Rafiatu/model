from flask import Flask, request
import json
import numpy as np
import pickle


SAVED_MODEL_PATH = "classifier.pkl"
classifier = pickle.load(open(SAVED_MODEL_PATH, "rb"))


def __process_input(request_data: str) -> np.array:
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    assert len(parsed_body) == 1 and len(parsed_body[0] == 13), "'inputs' must be a 1-d array with 13 parameters"
    return parsed_body


app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict() -> str:
    """

    :return:
    """
    try:
        input_params = __process_input(request.data)
        predictions = classifier.predict(input_params)

        return json.dumps({"predicted_class": predictions.tolist()}), 200
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except Flask.er:
        return json.dumps({"error": "PREDICTION FAILED"}), 500
