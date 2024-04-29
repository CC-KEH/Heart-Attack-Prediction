from src.Project4.config.configuration import Configuration_Manager
from src.Project4.components.data_ingestion import Data_Ingestion
from src.Project4.utils.common import logger


STAGE_NAME = 'Data Ingestion Stage'


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_Manager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = Data_Ingestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_data()


if __name__ == "__main__":
    try:
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e
