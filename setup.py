from setuptools import setup
from typing import List


# Declaring varibles for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="MANIKANTA"
DESCRIPTION="This is a first FSDS Nov batch Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:

    """
    Description: This function is going to return list of requirements
    mention in requirements.txt file

    return This function is going to retun a list which contain nameof libraries mentioned in requirements.txt file
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list() 

)


if __name__ =="__main__":
    print(get_requirements_list())