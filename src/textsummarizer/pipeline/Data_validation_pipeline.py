from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.Data_validation_component import DataValidation
from textsummarizer.entity.config_entity import DataValidationConfig

class DataValidationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            validaton_config=config.get_data_validation_config()
            obj=DataValidation(config=validaton_config)
            obj.validate_all_file_exists()
        except Exception as e:
            raise e