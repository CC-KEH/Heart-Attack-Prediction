import pandas as pd
from src.Project4.entity.config_entity import Data_Validation_Config


class Data_Validation:
    def __init__(self,config: Data_Validation_Config):
        self.config = config
        
    def validate_data(self) -> bool:
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                else:
                    validation_status = True
                with open(self.config.STATUS_FILE,'r') as f:
                        f.write(f'Validation Status: {validation_status}')                        
        except Exception as e:
            raise e            