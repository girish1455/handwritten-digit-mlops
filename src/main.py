from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI()

model = joblib.load("models/model.pkl")

class DigitInput(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "Handwritten Digit Detection API running"}

@app.post("/predict")
def predict(data: DigitInput):

    arr = np.array(data.features)
    arr = arr.reshape(1, -1)

    prediction = model.predict(arr)

    return {"prediction": int(prediction[0])}