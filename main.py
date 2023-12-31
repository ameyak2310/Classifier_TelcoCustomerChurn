""" 
Flask app to serve churn model.
"""

# Libraries
import pickle
import pandas as pd
from flask import Flask, request, jsonify

# Third party
from src.predict_single import predict_single


app = Flask("churn")

with open("bin/churn-model.bin", "rb") as f_in:
    """Loads encoder and model from binaries
    """
    dv, model = pickle.load(f_in)


@app.route("/predict", methods=["POST"])
def predict():
    """Prediction function

    Returns:
        dict: Returns probability and decesion.
    """
    payload = dict(request.get_json())
    prediction = predict_single(df=pd.DataFrame([payload]), dv=dv, model=model)
    churn = prediction >= 0.5
    result = {"PROBABILITY": float(prediction[0]), "VERDICT": bool(churn)}
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=9696)
