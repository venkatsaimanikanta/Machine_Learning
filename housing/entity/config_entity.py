from collections import namedtuple


DataIngestionConfig = namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])


### schema_file_path means How many No.of columns is there & what are thier data types and that path i'm going to specify

DataValidationConfig = namedtuple("DataValidationConfig",["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room",
                                                                   "transformed_train_dir",
                                                                   "transformed_test_dir",
                                                                   "preprocessed_object_filepath"])

### In Datatransformation steps, We are going to generate a pickle file and pickling object of feature engineering used in the prediction pipeline

## Now Specify column for Model Training.

ModelTraingConfig = namedtuple("ModelTraingConfig",["trained_model_file_path","base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_file_path","time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig",["export_dir_path"])