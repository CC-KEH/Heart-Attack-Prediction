from pathlib import Path
import os

CONFIG_FILE_PATH = Path('config/config.yaml')
PARAMS_FILE_PATH = Path('params.yaml')
SCHEMA_FILE_PATH = Path('schema.yaml')

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/CC-KEH/Heart-Attack-Prediction.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="CC-KEH"
os.environ["MLFLOW_TRACKING_PASSWORD"]="b0ca75eb844047a323c32834ca8cc3c7bf97c61e"