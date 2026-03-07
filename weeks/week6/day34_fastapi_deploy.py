#  since ipynb file cannot run fastapi server directly, we create a separate py file for it
from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
import uvicorn

# --- Define Input Schema ---
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# --- Load Model ---
model = joblib.load("models/rf_model_20251101_1705.joblib")

# --- Initialize App ---
app = FastAPI(title="Iris Classifier API", version="1.0")

@app.post("/predict")
def predict(data: IrisInput):
    df = pd.DataFrame([data.dict().values()], columns=data.dict().keys())
    pred = model.predict(df)[0]
    return {"prediction": pred}

# --- Run (local server) ---
# uvicorn.run(app, host="0.0.0.0", port=8000)
