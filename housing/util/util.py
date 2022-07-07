from ast import Str
import yaml
from housing.exception import HousingException
import os,sys

## Util is kind of helper function , It is used when it is required & it will be used in multiple places. 
## Whenever we are declaring any helper function (like create a pickle object ,how to load pickle object).Those kind of functions we will write inside util file.

def read_yaml_file(file_path:str)->dict:
    """
    reads a YAML file and returns the contents as a dictionary
    file_path: str
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e