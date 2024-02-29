from src.ChickenClassf.constants import *
from src.ChickenClassf.utils.common import read_yaml, create_directories
from src.ChickenClassf.entity.config_entity import (DataIngestionConfig,
                                                    PrepareBaseModelConfig)


class ConfigManager:
    def __init__(self,
                config_path = CONFIG_FILE_PATH,
                params_path = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        create_directories([self.config.artifact_roots])
        
        
    def get_data_ingetion_config(self) -> DataIngestionConfig:
        config= self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingetion_config= DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )        
        
        return data_ingetion_config
    
    def get_prepare_base_Model_config(self) -> PrepareBaseModelConfig:
        config= self.config.prepare_base_model
        create_directories([config.root_dir])
        
        data_ingetion_config= PrepareBaseModelConfig(
            root_dir= config.root_dir,
            base_model_path =config.base_model_path,
            updated_base_model_path= config.updated_base_model_path,
            params_image_size= self.params.IMAGE_SIZE,
            params_learning_rate= self.params.LEARNING_RATE,
            params_include_top= self.params.INCLUDE_TOP,
            params_weights= self.params.WEIGHTS,
            params_classes= self.params.CLASSES
        )
        return data_ingetion_config
    
        