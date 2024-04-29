from src.Project4.config.configuration import Configuration_Manager
from src.Project4.components.model_trainer import Model_Trainer
from src.Project4.utils.common import logger


STAGE_NAME = 'Model Trainer Stage'


class ModeLTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = Configuration_Manager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = Model_Trainer(config=model_trainer_config)
        model_trainer.train_model()


if __name__ == "__main__":
    try:
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
        obj = ModeLTrainerTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e
