import pickle
import pandas as pd

with open('Models/lightgbm_model.pkl', 'rb') as f:
    model = pickle.load(f)


MODEL_VERSION = '1.0.0'

class_label = model.classes_.tolist()

def predict_output(user_input):

    df = user_input

    pred = int(model.predict(df)[0])

    prob = model.predict_proba(df)[0]

    confidence = float(max(prob))

    class_label = ["No Default", "Default"]

    class_probs = {
        label: round(float(p), 4)
        for label, p in zip(class_label, prob)
    }

    risk = "High Risk" if pred == 1 else "Low Risk"

    return {
        "prediction": pred,
        "risk": risk,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }