from joblib import load
import cv2
import numpy as np
import tensorflow as tf
import keras
import os
import json
def predictWithModel(file):
    model = keras.models.load_model('App/MLApp/ModeloRedesConv/model')
    muestra = [file]
    nRows = 150  # Ancho
    nCols = 150  # Altura
    channels = 3  # Canales de color RGB-3
    muestra_predecir=[]
    for image in muestra:
        array = np.asarray(bytearray(image), dtype=np.uint8)
        lectura=cv2.imdecode(array, cv2.IMREAD_COLOR)
        
        muestra_predecir.append(cv2.resize(lectura, (nRows, nCols), interpolation=cv2.INTER_CUBIC))
    muestra_predecir=np.array(muestra_predecir)
    diccionario= {1:'Nublado',2:'Lluvioso',3:'Amanecer/Atardecer',4:'Soleado'}
    predicciones=model.predict(muestra_predecir)
    classes = np.argmax(predicciones, axis = 1)
    print(predicciones,classes,"csaiojcsa",predicciones[0][0])
    
    imageResultList = []
    for i, clase in enumerate(classes):
        imageResults = {}
        imageResults["Prediction"] = diccionario[clase]
        imageResults["Accuracy"] = float(predicciones[i][clase])
        imageResultList.append(imageResults)
        
    response = imageResultList
    return response
