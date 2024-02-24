import os,sys
from src.Project4.utils.common import logger
from src.Project4.components.data_transformation import Data_Transformation
from src.Project4.entity.config_entity import Data_Transformation_Config
from src.Project4.config.configuration import Configuration_Manager


STAGE_NAME = 'Data Transformation'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):    
        try:
            with open('artifacts/data_validation/status.txt','r') as f:
                status = f.read().split(" ")[-1]
            
            if(status==True):
                config = Configuration_Manager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = Data_Transformation(config=data_transformation_config)
                data_transformation.transform_data()
            else:
                raise Exception('Invalid Data Schema')
            
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e
    