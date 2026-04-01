import pandas as pd


class Data:

  def __init__(self):
    self.data = None
    self.path = None

  def load_data(self,path):
    self.path = path
    self.data = pd.read_csv(path)
    return self.data
  
  def to_df(self,model,r2,mse,mae,rmse):

    res_dict = {
      "model": model,
      "r2_score": r2,
      "mse": mse,
      "mae": mae,
      "rmse": rmse
    }

    return pd.DataFrame(res_dict,index=[0])
  
  def save_model(self,df_list):
    result_df = pd.concat(df_list,ignore_index=True)
    result_df.to_csv("model_evaluation_results.csv",index=False)


  