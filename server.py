from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import SampleModelParams
import prediction as MLApi

app = FastAPI()

origins = [
  "*",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
async def index():
  return {
    "condition": "OK",
    "model_version": "0.1.0"
  }

@app.post("/predict")
async def predict_route(payload : SampleModelParams):
  # TODO: Change this based on your model parameters
  result = MLApi.make_prediction(
    gender=payload.gender,
    age=payload.age,
  )

  if result:
    response = {"prediction": "Positive"}
  else:
    response = {"prediction": "Negative"}
  return response
