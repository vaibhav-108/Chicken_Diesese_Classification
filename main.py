from src.ChickenClassf import logger #to create a logs
from src.ChickenClassf.pipeline.stage_01_Data_Ingestion import DataIngetionPipeline   

logger.info("Welcome to run Chicken Classf")
stage = 'Data INGESTION PIPELINE'


try:
        
        logger.info(f">>>>> STAGE 01{stage} <<<<<<")

        data_ingestion_pipeline_obj = DataIngetionPipeline()
        data_ingestion_pipeline_obj.DataPipeline()
        logger.info(f" Data ingestion pipeline is done!")
        
except Exception as e:
        logger.exception(e)
        raise e