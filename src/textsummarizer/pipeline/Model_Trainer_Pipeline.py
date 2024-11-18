from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.Model_trainer_component import ModelTrainer
from textsummarizer.entity.config_entity import ModelTrainerConfig

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            trainer_config=config.get_model_trainer_config()
            obj=ModelTrainer(config=trainer_config)
            obj.train()
        except Exception as e:
            raise e