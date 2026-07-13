from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uvicorn
import pandas as pd
import pickle
from pathlib import Path
from schema.user_input import Applicant
from schema.prediction_response import PredictionResponse
from utils.feature_engineering import create_features
from utils.binary_mapping import apply_binary_mapping
from utils.predict import predict_output, MODEL_VERSION


with open('Models/lightgbm_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('Models/preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home Credit Risk API"}

# for machine readable
@app.get("/health")
def health_check():
    return {
        'status' : 'OK',
        'version' : MODEL_VERSION, 
        'model_loaded' : model is not None
    }

@app.post("/predict", response_model=PredictionResponse)
def predict(applicant: Applicant):

    df = pd.DataFrame([applicant.model_dump()])

    df = create_features(df)

    df = apply_binary_mapping(df)

    df = preprocessor.transform(df)


    # return predict_output(df)
    try:
        prediction = predict_output(df)
        return prediction
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))


 