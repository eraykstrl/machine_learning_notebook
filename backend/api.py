from fastapi import FastAPI
from backend.model import Data
from pydantic import ValidationError


app = FastAPI()

@app.get('/')
async def root():
  return {"message" : "Connection is successful"}


@app.get('/data/{data}')
async def read_data(payload : dict):

  try:
    validated_data = Data(**payload)

    return {
      "status" : "success",
      "message" : "Validation is sucessfull. ",
      "data_id" : validated_data.data_id
    }
  
  except ValidationError as e:

    return {
      "status" : "error",
      "message" : "An error has occured. ",
      "details" : e.errors()
    }
  
  except Exception as e:
    return {
      "status" : "error",
      "message" : "Beklenmedik bir hata oluştu {e}"
    }
  

@app.get('/result/{result}')
async def get_result():

  try:
    



