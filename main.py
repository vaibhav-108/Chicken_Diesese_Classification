from src.ChickenClassf import logger #to create a logs
from src.ChickenClassf.pipeline.stage_01_Data_Ingestion import DataIngetionPipeline 
from src.ChickenClassf.pipeline.stage_02_Prepare_base_model import PrepareBaseModelTrainingPipeline

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




STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.BaseModelPipeline()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


