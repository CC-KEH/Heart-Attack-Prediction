from src.Project4.config.configuration import Configuration_Manager
from src.Project4.components.model_evaluation import Model_Evaluation
from src.Project4.utils.common import logger


STAGE_NAME = 'Model Evaluation Stage'

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = Configuration_Manager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = Model_Evaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
        
        
if __name__ == "__main__":
    try:
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Started <<<<<<<')
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>> STAGE {STAGE_NAME} Completed <<<<<<<\n\nx=============x')
    except Exception as e:
        logger.exception(e)
        raise e