from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, \
ModelPusherConfig, ModelTrainerConfig, TrainingPipelineConfig

from housing.util.util import read_yaml_file
from housing.exception import HousingException
import os,sys
from housing.logger import logging

from housing.constant import *     ## * means declare all the files inside constant.py file



class Configuration:

    def __init__(self,
        config_file_path = CONFIG_FILE_PATH,
        current_time_stamp:str = CURENT_TIME_STAMP
    ) -> None:
        self.config_info = read_yaml_file(config_file_path)
        self.get_training_pipeline_config  = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        pass

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        pass    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) -> ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e

