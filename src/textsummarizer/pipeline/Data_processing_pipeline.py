from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.Data_transformation_component import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            transformation_config=config.get_data_transformation_config()
            obj=DataTransformation(config=transformation_config)
            obj.convert()

        except Exception as e:
            raise e