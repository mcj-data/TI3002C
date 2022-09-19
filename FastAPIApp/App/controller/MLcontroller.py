from fastapi import APIRouter, File, UploadFile, Form
from App.MLapp.TrainModel import model as TrainModel
from App.MLapp.Predict import predictWithModel
from App.MLapp.RequestTypes.prediction import ModelPredictionInput
from App.MLapp.ModeloRedesConv.TrainModel import TrainModel as TrainRedesConv
from App.MLapp.ModeloRedesConv.Predict import predictWithModel as PredictRedesConv

from typing import Union

router = APIRouter(prefix="/api/v1/ML")

@router.get("/handshake")
async def handshake():
    print(UploadFile.__dict__)
    return {"hi":"hello"}

@router.get("/TrainModel")
async def model():
    return TrainModel()
@router.get("/TrainRedesConv")
async def redesModel():
    return TrainRedesConv()

@router.post("/predictWithModel")
async def predictModel(ModelPredictionInput: ModelPredictionInput):
    return predictWithModel(ModelPredictionInput.X)
@router.post("/TrainRedesConv/Predict")
async def redesModelPredict(file: UploadFile = File(...)):
    try:
        with open(f"App/persist/{file.filename}", 'wb') as f:
            with open(f"App/persist/{file.filename}", 'rb') as input_file:
                while contents := file.file.read(1024 * 1024):
                    f.write(contents)
                    file.file.close()
                    return PredictRedesConv(input_file.read())
    except TypeError as e:
        print(e)
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    return {"message": f"Successfully uploaded {file.filename}"}
    

@router.post("/Model2/upload")
def upload(file: UploadFile = File(...)):
    try:
        with open(f"App/persist/{file.filename}", 'wb') as f:
            while contents := file.file.read(1024 * 1024):
                f.write(contents)
    except Exception as e:
        print(e)
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    return {"message": f"Successfully uploaded {file.filename}"}