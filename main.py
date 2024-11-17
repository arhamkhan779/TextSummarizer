from textsummarizer.logging import logger
from textsummarizer.pipeline.Data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME="DATA INGESTION STAGE"

try:
    logger.info(f"{STAGE_NAME} has Started")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} has completed")
    
except Exception as e:
    raise e