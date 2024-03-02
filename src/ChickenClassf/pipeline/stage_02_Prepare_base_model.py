from ChickenClassf.config.configuration import ConfigManager
from ChickenClassf.components.prepare_base_model import PrepareBaseModel
from ChickenClassf import logger

STAGE_NAME ="PPREPARE_BASE_MODEL"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def BaseModelPipeline(self):
        
        try:
            config = ConfigManager()
            prepare_base_model_config = config.get_prepare_base_Model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e


if __name__ == "__main__":

    try: 
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.BaseModelPipeline()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
            logger.exception(e)
            raise e
