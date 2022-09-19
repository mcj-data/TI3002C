import os
import gc
import cv2
import random
import numpy as np
from tensorflow.keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten
from joblib import dump


def TrainModel():
        
    cloud_set = ['App/MLapp/ModeloRedesConv/data/{}'.format(i) for i in os.listdir('App/MLapp/ModeloRedesConv/data') if 'cloudy' in i]
    rain_set = ['App/MLapp/ModeloRedesConv/data/{}'.format(i) for i in os.listdir('App/MLapp/ModeloRedesConv/data') if 'rain' in i]
    sunrise_set = ['App/MLapp/ModeloRedesConv/data/{}'.format(i) for i in os.listdir('App/MLapp/ModeloRedesConv/data') if 'sunrise' in i]
    sunshine_set = ['App/MLapp/ModeloRedesConv/data/{}'.format(i) for i in os.listdir('App/MLapp/ModeloRedesConv/data') if 'shine' in i]

    # 2.) Aleatorizar las imagenes antes del entrenamiento
    random.shuffle(cloud_set)
    random.shuffle(rain_set)
    random.shuffle(sunrise_set)
    random.shuffle(sunshine_set)

    # 3.) Definición de los datasets para entrenamiento y testing
    train_set = cloud_set[:150] + rain_set[:150] + sunrise_set[:150] + sunshine_set[:150]
    test_set = cloud_set[150:] + rain_set[150:] + sunrise_set[:150] + sunshine_set[:150]

    # 4.) Eliminación de la memoria de Datasets que no usaremos
    del cloud_set, rain_set, sunrise_set, sunshine_set
    gc.collect()
    # 5.) Pre-Procesamiento de las imagenes
    nRows = 150  # Ancho
    nCols = 150  # Altura
    channels = 3  # Canales de color RGB-3

    # 6.) Etiquetado de los datasets para entrenamiento y testing
    X_train = []
    X_test = []
    y_train = []
    y_test = []

    # 7.) Leer y etiquetar cada imagen del dataset de entrenamiento
    for image in train_set:
        try:
            X_train.append(cv2.resize(cv2.imread(image, cv2.IMREAD_COLOR), (nRows, nCols), interpolation=cv2.INTER_CUBIC))
            if 'cloudy' in image:
                y_train.append(1)
            elif 'rain' in image:
                y_train.append(2)
            elif 'sunrise' in image:
                y_train.append(3)
            elif 'shine' in image:
                y_train.append(4)
        except Exception:
            print('Failed to format: ', image)

    # 8.) Leer y etiquetar cada imagen del dataset de testing

    diccionario= {1:'Nublado',2:'Lluvioso',3:'Amanecer/Atardecer',4:'Soleado'}

    for image in test_set:
        try:
            X_test.append(cv2.resize(cv2.imread(image, cv2.IMREAD_COLOR), (nRows, nCols), interpolation=cv2.INTER_CUBIC))
            if 'cloudy' in image:
                y_test.append(1)
            elif 'rain' in image:
                y_test.append(2)
            elif 'sunrise' in image:
                y_test.append(3)
            elif 'shine' in image:
                y_test.append(4)
        except Exception:
            print('Failed to format: ', image)

    # 9.) Liberación de memoria
    del train_set, test_set
    gc.collect()

    # 10.) Conversión a arrays tipo Numpy
    X_train = np.array(X_train)
    X_test = np.array(X_test)
    y_train = np.array(y_train)
    y_test = np.array(y_test)

    # 11.) Conversión a tipo categórica
    try:
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
    except ValueError:
        pass
    # 12.) Definición del modelo convolucional
    model = Sequential()
    model.add(Conv2D(32, kernel_size=3, activation='relu', input_shape=(150, 150, 3)))
    model.add(MaxPooling2D(2, 2))
    model.add(Conv2D(64, kernel_size=3, activation='relu'))
    model.add(MaxPooling2D(2, 2))
    model.add(Conv2D(128, kernel_size=3, activation='relu'))
    model.add(MaxPooling2D(2, 2))
    model.add(Conv2D(256, kernel_size=3, activation='relu'))
    model.add(MaxPooling2D(2, 2))
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(5, activation='softmax'))

    # 13.) Resumen del modelo
    print(model.summary())

    # 14.) Entrenamiento del modelo
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10)
    model.save('App/MLApp/ModeloRedesConv/model')
