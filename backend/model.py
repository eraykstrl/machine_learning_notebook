from pydantic import BaseModel,ValidationError
from typing import List

class Feature(BaseModel):
  feature_name : str
  feature_value : int | float 
  
class Target(BaseModel):
  target_name:str
  target_value : int | float

class Data(BaseModel):
  data_id : str
  features : List[Feature]
  targets : List[Target]


class Model(BaseModel):
  model_name : str
  model_results : List[Result]


class Result(BaseModel):
  mae : float | None
  rmse : float | None
  r2_score : float | None
  accuracy : float | None
  loss : float | None

