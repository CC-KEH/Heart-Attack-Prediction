from sklearn.model_selection import train_test_split
from src.Project4.utils.common import logger
from src.Project4.entity.config_entity import Data_Transformation_Config
import pandas as pd


class Data_Transformation:
    def __init__(self,config: Data_Transformation_Config):
        self.config = config

    def transform_data(self):
        try:
            data = pd.read_csv(self.config.data_path)
            train_data,test_data = train_test_split(data,test_size=0.2,random_state=42,shuffle=True)
            train_data.to_csv(self.config.data_path,"train.csv",index=False)
            test_data.to_csv(self.config.data_path,"test.csv",index=False)
            
            logger.info('Splitted the data into train and test')
            logger.info(f'Train data shape: {train_data.shape}')
            logger.info(f'Test data shape: {test_data.shape}')
        except Exception as e:
            raise e
        