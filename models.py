from pydantic import BaseModel

class SampleModelParams(BaseModel):
  # TODO: tune based on your ML model params
  # sample gender and age are provided bellow
  gender : str
  age : int
