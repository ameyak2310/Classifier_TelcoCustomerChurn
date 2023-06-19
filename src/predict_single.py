""" Prediction function
"""

def predict_single(df, dv, model):
    """Prediction Algorithm

    Args:
        df (DataFrame): Payload
        dv (Vectorizer): Encoder
        model (model): Trained model

    Returns:
        y_prob (float): Probability of Churn
    """
    categorical_features = [
        "gender",
        "seniorcitizen",
        "partner",
        "dependents",  #'customerid',
        "phoneservice",
        "multiplelines",
        "internetservice",  #'tenure',
        "onlinesecurity",
        "onlinebackup",
        "deviceprotection",
        "techsupport",
        "streamingtv",
        "streamingmovies",
        "contract",
        "paperlessbilling",
        "paymentmethod",
        #'monthlycharges', 'totalcharges',
        # 'churn'
    ]

    numerical_features = ["tenure", "monthlycharges", "totalcharges"]

    X = df[categorical_features + numerical_features].to_dict(orient="records")
    X_en = dv.transform(X)

    y_prob = model.predict_proba(X_en)[:, 1]
    return y_prob
