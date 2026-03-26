from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
import numpy as np

class Model:

  def __init__(self, model):
    self.model = model

  def fit(self,X_train,y_train):
    return self.model.fit(X_train,y_train)

  def predict(self,X_test):
    return self.model.predict(X_test)
  
  def evaluate(self,y,y_pred):
    return {
      "mse": mean_squared_error(y, y_pred),
      "mae": mean_absolute_error(y, y_pred),
      "r2": r2_score(y, y_pred),
      "rmse" : np.sqrt(mean_squared_error(y, y_pred))
    }