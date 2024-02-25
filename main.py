from src.Project4.utils import logger
from src.Project4.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Project4.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.Project4.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.Project4.pipeline.stage_04_model_trainer import ModeLTrainerTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx============================x')
except Exception as e:
    logger.exception(e)
    raise e
        

STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx============================x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Transformation'

try:
    logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx============================x')
except Exception as e:
    logger.exception(e)
    raise e
    

STAGE_NAME = 'Model Trainer Stage'

try:
    logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
    obj = ModeLTrainerTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx============================x')
except Exception as e:
    logger.exception(e)
    raise e  