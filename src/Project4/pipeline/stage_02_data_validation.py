from src.Project4.config.configuration import Configuration_Manager
from src.Project4.components.data_validation import DataValidation
from src.Project4.utils.common import logger


STAGE_NAME = 'Data Validation Stage'


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_Manager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_data()


if __name__ == "__main__":
    try:
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e
