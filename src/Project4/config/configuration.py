from src.Project4.constants import *
from src.Project4.utils.common import read_yaml,create_directories
from src.Project4.entity.config_entity import Data_Ingestion_Config,Data_Validation_Config,Data_Transformation_Config,Model_Trainer_Config,Model_Evaluation_Config

class Configuration_Manager:
    def __init__(self,config_file_path = CONFIG_FILE_PATH,params_file_path = PARAMS_FILE_PATH,schema_file_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self) -> Data_Ingestion_Config:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = Data_Ingestion_Config(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self)->Data_Validation_Config:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])
        data_validaton_config = Data_Validation_Config(root_dir=config.root_dir,all_schema=schema,STATUS_FILE=config.STATUS_FILE,unzip_dir=config.unzip_dir)
        return data_validaton_config
    
    def get_data_transformation_config(self) -> Data_Transformation_Config:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = Data_Transformation_Config(root_dir=config.root_dir,data_path=config.data_path)
        return data_transformation_config
    
    def get_model_trainer_config(self)->Model_Trainer_Config:
        config = self.config.model_trainer
        schema = self.schema.TARGET_COLUMN
        params = self.params
        create_directories([config.root_dir])
        model_trainer_config = Model_Trainer_Config(root_dir=config.root_dir,train_path=config.train_path,test_path=config.test_path,target_column=schema,params=params)
        return model_trainer_config
    
    def get_model_evaluation_config(self)->Model_Evaluation_Config:
        config = self.config.model_evaluation
        schema = self.schema.TARGET_COLUMN
        params = self.params #! Fix the issue of params
        
        create_directories([config.root_dir])
        
        model_evaluation_config = Model_Evaluation_Config(root_dir=config.root_dir,
                                                          test_data_path=config.test_data_path,
                                                          model_path=config.model_path,
                                                          all_params=params,
                                                          metric_file_name=config.metric_file_name,
                                                          mlflow_uri="https://dagshub.com/CC-KEH/Heart-Attack-Prediction.mlflow",
                                                          target_column=schema.name)
        return model_evaluation_config
    