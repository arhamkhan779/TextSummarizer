import os
import urllib.request as request
import zipfile
from textsummarizer.logging import logger
from textsummarizer.utils.common import get_size
from pathlib import Path
from textsummarizer.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            file_name,header=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"{file_name} download with following info: \n {header}")
        
        else:
            logger.info(f"file already exist of size {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        '''
        Zip_path: str
        extract zip file into directory
        return none
        '''
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)