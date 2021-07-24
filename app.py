from flask import Flask, request
import json
import pickle
from process_input import process_input


SAVED_MODEL_PATH = "classifier.pkl"
classifier = pickle.load(open(SAVED_MODEL_PATH, "rb"))


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home() -> str:
    """
    Homepage for this API.
    :return: Basic info about the API. A short introductory message
    """
    return ("""Welcome to Rafihatu Bello's house price prediction API. This API has only one useful endpoint \n
              Predict House prices via the endpoint https://rafi-predictions.herokuapp.com/predict using a POST request.\n 
              Inputs should be a list of 13 numbers. For more info, visit https://github.com/Rafiatu/model"""), 200


@app.route('/predict', methods=['POST'])
def predict() -> str:
    """
    predicts the prices of houses using the trained model based on the inputs passed in the request.
    :return: predicted class for the request
    """
    try:
        input_params = process_input(request.data)
        predictions = classifier.predict(input_params)
        return json.dumps({"predicted_price": predictions.tolist()}), 200
    except (KeyError, json.JSONDecodeError, AssertionError):
        return json.dumps({"error": "CHECK INPUT"}), 400
    except Exception:
        return json.dumps({"error": "PREDICTION FAILED"}), 500

if __name__ == '__main__':
    app.run(debug=True)