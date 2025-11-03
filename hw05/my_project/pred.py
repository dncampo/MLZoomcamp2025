from fastapi import FastAPI
from typing import Dict, Any
import pickle

app = FastAPI(title="Lead Score prob")

def load_pipe():
    filename = "pipeline_v1.bin"
    with open(filename, "rb") as f_in:
        print(f"model: {filename} has been loaded")
        return pickle.load(f_in)
    raise FileNotFoundError("Bin file not found")

pipeline = load_pipe()

def pred_one(record):
    res = pipeline.predict_proba(record)[0, 1]
    return float(res)

@app.post('/predict')
def predict(record: Dict[str, Any]):
    pred = pred_one(record)
    return {
        "Score": pred,
        "Subscription": bool(pred >= 0.5) 
    }



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
