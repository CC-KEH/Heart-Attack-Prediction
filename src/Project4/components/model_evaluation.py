from src.Project4.utils.common import save_json
from sklearn.metrics import accuracy_score,mean_squared_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import joblib
from src.Project4.entity.config_entity import Model_Evaluation_Config
from pathlib import Path
import pandas as pd


class Model_Evaluation:
    def __init__(self,config:Model_Evaluation_Config):
        self.config = config
    
    def evaluate_metrics(self,actual,pred):
        accuracy = accuracy_score(actual,pred)
        mse = mean_squared_error(actual,pred)
        return accuracy,mse

    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        X_test = test_data.drop([self.config.target_column],axis=1)
        y_test  = test_data[[self.config.target_column]]
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            predictions = model.predict(X_test)
            (accuracy,mse) = self.evaluate_metrics(y_test,predictions)
            
            # Save Metrics as local
            
            scores = {"Accuracy": accuracy,"Mean Squared Error": mse}
            save_json(path=Path(self.config.metric_file_name),data=scores)
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("Accuracy",accuracy)
            mlflow.log_metric("Mean Squared Error",mse)
            
            # Model registry does not work with file store
            if tracking_url_type_store !='file':
                mlflow.sklearn.log_model(model,"model",registered_model_name="Logistic Regression Model")
            else:
                mlflow.sklearn.load_model(model,'model')
            
        