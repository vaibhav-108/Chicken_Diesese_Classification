from src.ChickenClassf.config.configuration import ConfigManager
from src.ChickenClassf.entity.config_entity  import DataIngestionConfig
from src.ChickenClassf.components.data_ingestion import DataIngestion
from src.ChickenClassf import logger

stage ="DATA_INGESTION_STAGE"

class DataIngetionPipeline:
    def __init__(self):
        pass
    
    def DataPipeline(self):
        
            config_manager = ConfigManager()
            data_ingetion_config = config_manager.get_data_ingetion_config()
            data_ingestion = DataIngestion(config= data_ingetion_config)
            data_ingestion.download_file()
            data_ingestion.unzip_file()
        
        
# if __name__ == "__main__":
#     try:
        
#         logger.info(f">>>>> STAGE 01{stage} <<<<<<")

#         data_ingestion_pipeline_obj = DataIngetionPipeline()
#         data_ingestion_pipeline_obj.DataPipeline()
#         logger.info(f" Data ingestion pipeline is done!")
        
#     except Exception as e:
#         logger.exception(e)
#         raise e