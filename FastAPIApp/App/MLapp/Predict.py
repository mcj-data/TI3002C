from joblib import load

def predictWithModel(X):
    clf = load('App/MLApp/model.joblib') 
    y_pred = clf.predict(X)
    return y_pred.tolist()
