from  ChickenClassf.config.configuration import ConfigManager
from  ChickenClassf.components.model_evaluation import Evaluation
from  ChickenClassf import logger



STAGE_NAME = "MODEL_EVALUATION"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def ModelEvalPipeline(self):
        
        try:
            config = ConfigManager()
            val_config = config.get_validation_config()
            evaluation = Evaluation(val_config)
            evaluation.evaluation()
            evaluation.save_score()

        except Exception as e:
            raise e
        
        
if __name__ == "__main__":
    
    try: 
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_eval = ModelEvaluationPipeline()
        model_eval.ModelEvalPipeline()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e