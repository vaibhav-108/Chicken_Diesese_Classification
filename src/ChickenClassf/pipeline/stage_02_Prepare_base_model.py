from src.ChickenClassf.config.configuration import ConfigManager
from src.ChickenClassf.entity.config_entity  import PrepareBaseModelConfig
from src.ChickenClassf.components.prepare_base_model import PrepareBaseModel
from src.ChickenClassf import logger

stage ="PPREPARE_BASE_MODEL"

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



       