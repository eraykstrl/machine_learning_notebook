from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OrdinalEncoder
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd


class Preprocessing:

  def __init__(self):

    self.X_scaler = StandardScaler()
    self.y_scaler = StandardScaler()
    self.X_encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
    self.categorical_cols = None


  def split_X_y(self,df,target):
    X = df.drop(target,axis = 1)
    y = df[target]
    return X,y


  def split_data(self,X,y,test_size = 0.2,random_state = 42):
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = test_size,random_state = random_state)
    return X_train,X_test,y_train,y_test


  def impute(self,method,X_train,X_test,y_train,y_test):

    numeric_cols_train = X_train.select_dtypes(include = ["int64","float64"]).columns

    
    imputer = SimpleImputer(strategy = method,missing_values = np.nan)
    X_train[numeric_cols_train]= imputer.fit_transform(X_train[numeric_cols_train])
    X_test[numeric_cols_train]= imputer.transform(X_test[numeric_cols_train])

    return X_train,X_test,y_train,y_test

  def feature_engineering(self,X,y):
    pass

  def feature_selection(self,X,y):
    pass

  def normalize(self,X):
    pass

  def encode(self,X_train,X_test,y_train,y_test):

    categorical_cols_train = X_train.select_dtypes(include = ["object","category"]).columns
    if len(categorical_cols_train) == 0:
      return X_train,X_test,y_train,y_test

    self.categorical_cols = list(categorical_cols_train)

    X_train = X_train.copy()
    X_test = X_test.copy()

    encoded_train = self.X_encoder.fit_transform(
      X_train.loc[:, self.categorical_cols].astype(str)
    )
    encoded_test = self.X_encoder.transform(
      X_test.loc[:, self.categorical_cols].astype(str)
    )

    encoded_train_df = pd.DataFrame(
      encoded_train,
      columns=self.categorical_cols,
      index=X_train.index,
    ).astype(float)
    encoded_test_df = pd.DataFrame(
      encoded_test,
      columns=self.categorical_cols,
      index=X_test.index,
    ).astype(float)

    X_train_encoded = pd.concat([
      X_train.drop(columns=self.categorical_cols),
      encoded_train_df
    ], axis=1)[X_train.columns]

    X_test_encoded = pd.concat([
      X_test.drop(columns=self.categorical_cols),
      encoded_test_df
    ], axis=1)[X_test.columns]

    return X_train_encoded, X_test_encoded, y_train, y_test


