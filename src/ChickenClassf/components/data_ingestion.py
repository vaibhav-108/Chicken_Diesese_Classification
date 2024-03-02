
import os
import urllib.request as request
import zipfile as zf
from ChickenClassf import  logger
from ChickenClassf.utils.common import get_size
from ChickenClassf.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            
            logger.info(f"{filename} download! with following info: \n{headers}")
    
        else:
            logger.info(f"{filename} already exists! of size {get_size(Path(self.config.local_data_file))} bytes")
            
    def unzip_file(self):
        unzip_dir= self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)
        

            
        with zf.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_dir)
        logger.info(f"{self.config.local_data_file} unzipped!")
        
            
    
        
        