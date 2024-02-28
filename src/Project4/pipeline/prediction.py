from src.Project4.utils import logger
from src.Project4.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Project4.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.Project4.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from src.Project4.pipeline.stage_04_model_trainer import ModeLTrainerTrainingPipeline
from src.Project4.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
import joblib
from pathlib import Path
import numpy as np
import pandas as pd


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
        
    def predict(self,data):
        prediction = self.model.predict(data)
        return prediction
    