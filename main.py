from textsummarizer.logging import logger
from textsummarizer.pipeline.Data_ingestion_pipeline import DataIngestionPipeline
from textsummarizer.pipeline.Data_validation_pipeline import DataValidationPipeline
from textsummarizer.pipeline.Data_processing_pipeline import DataTransformationPipeline
from textsummarizer.pipeline.Model_Trainer_Pipeline import ModelTrainingPipeline

STAGE_NAME="DATA INGESTION STAGE"

try:
    logger.info(f"{STAGE_NAME} has Started")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} has completed")
    
except Exception as e:
    raise e

STAGE_NAME="DATA VALIDATION STAGE"

try:
    logger.info(f"{STAGE_NAME} has Started")
    obj=DataValidationPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} has completed")
    
except Exception as e:
    raise e

STAGE_NAME="DATA TRANSFORMATION STAGE"

try:
    logger.info(f"{STAGE_NAME} has Started")
    obj=DataTransformationPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} has completed")
    
except Exception as e:
    raise e

STAGE_NAME="MODEL TRAINER STAGE"

try:
    logger.info(f"{STAGE_NAME} has Started")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} has completed")
except Exception as e:
    raise e