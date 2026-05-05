from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
import lightgbm as lgb
from machine_learning.data import Data
from machine_learning.preprocessing import Preprocessing
from machine_learning.model import Model



if __name__ == "__main__":

  data = Data()
  df = data.load_data('job_salary_prediction_dataset.csv')

  preprocessing = Preprocessing()
  X,y = preprocessing.split_X_y(df,'salary')
  X_train,X_test,y_train,y_test = preprocessing.split_data(X,y)
  X_train,X_test,y_train,y_test = preprocessing.encode(X_train,X_test,y_train,y_test)
  X_train,X_test,y_train,y_test = preprocessing.impute('mean',X_train,X_test,y_train,y_test)

  
  model_1 = Model(RandomForestRegressor())
  model_1.fit(X_train,y_train)

  model_2 = Model(xgb.XGBRegressor())
  model_2.fit(X_train,y_train)


  model_3 = Model(lgb.LGBMRegressor())
  model_3.fit(X_train,y_train)



  df_list = []
  for model in [model_1,model_2,model_3]:
    y_pred = model.predict(X_test)
    evaluation = model.evaluate(y_test,y_pred)
    dataframe= data.to_df(model=type(model.model).__name__,r2=evaluation['r2'],mse=evaluation['mse'],mae=evaluation['mae'],rmse=evaluation['rmse'])
    df_list.append(dataframe)

  data.save_model(df_list)

  print("Model evaluation results saved to model_evaluation_results.csv")



  





