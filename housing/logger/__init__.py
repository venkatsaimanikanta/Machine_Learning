import logging
from datetime import datetime
import os

## The Directory in which we are log our project
## Folder name as housing_logs
LOG_DIR ="housing_logs"

## Give us current time stamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

## create a File
LOG_FILE_NAME = F"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR,exist_ok= True)

LOG_FILE_PATH = os.path.join(LOG_DIR,LOG_FILE_NAME)
logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
)