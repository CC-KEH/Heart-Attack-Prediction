import os
import urllib.request as request
import zipfile
from src.Project4.utils.common import get_size, logger
from src.Project4.entity.config_entity import Data_Ingestion_Config
from pathlib import Path

class Data_Ingestion:
    def __init__(self,config: Data_Ingestion_Config):
        self.config = config
        
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename,header = request.urlretrieve(url=self.config.source_URL,filename=self.config.local_data_file)
            logger.info(f'Successfully downloaded data {filename} with following info: {header} at: {self.config.local_data_file}')
        else:
            logger.info(f'Data already exists of size {get_size(Path(self.config.local_data_file))}')
    
    def extract_zip_data(self):
        ''' Extracts the zip file
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)