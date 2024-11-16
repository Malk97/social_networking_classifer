from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import uvicorn
import numpy as np
from xgboost import Booster





# Load the model
try:
    xgb_model = Booster()
    xgb_model.load_model("G:\Malk\Qafza\Malk Al-Jarrah_Task2\Dep_FastApi_Network\Model\xgb_model.json")
except Exception as e:
    raise RuntimeError(f"Failed to load model: {e}")

app = FastAPI()

# Define the request schema
class InputData(BaseModel):
    Age: float
    EstimatedSalary: float
    Gender: str

# Endpoint for prediction
@app.post("/predict")
async def predict(data: InputData):
    try:
        if data.Gender=="female":
            GEn=0
        else:
            GEn=1

        input_data = np.array([[GEn, data.Age, data.EstimatedSalary]])
        prediction = xgb_model.predict(input_data)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": str(e)}

if __name__=="__main__":
    uvicorn.run(app)