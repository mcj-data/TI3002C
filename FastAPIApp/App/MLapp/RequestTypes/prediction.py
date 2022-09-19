from array import array
from pydantic import BaseModel
from typing import Union, Optional

class ModelPredictionInput(BaseModel):
    X: list
    description: Optional[str]
    
