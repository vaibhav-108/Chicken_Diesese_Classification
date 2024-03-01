from src.ChickenClassf.config.configuration import ConfigManager
from src.ChickenClassf.components.prepare_callbacks import PrepareCallbacks
from src.ChickenClassf.components.prepare_training import Training
from src.ChickenClassf import logger


stage ="TRAINING_MODEL"

class PrepareTrainingPipeline:
    def __init__(self):
        pass
    
    def TrainingPipeline(self):


        try:
            config = ConfigManager()
            prepare_callbacks_config = config.get_prepare_callback_config()
            prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
            callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

            training_config = config.get_training_config()
            training = Training(config=training_config)
            training.get_base_model()
            training.train_valid_generator()
            training.train(
                callback_list=callback_list
            )
            
        except Exception as e:
            raise e