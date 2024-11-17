from textsummarizer.config.configuration import ConfigurationManager
from textsummarizer.components.Data_ingestion_component import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            config=ConfigurationManager()
            ingestion_config=config.get_data_ingestion_config()
            obj=DataIngestion(config=ingestion_config)
            obj.download_data()
            obj.extract_zip_file()

        except Exception as e:
            raise e