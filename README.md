## Start Machine_Learning Project.

### Requirement.

1. [GitHub Account](https://github.com/)
2. [Heroku Account](https://id.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT DOCUMENTATION](https://git-scm.com/doc)

Creating conda environment
```
conda create -p venv python==3.7 -y
```


```
conda activate venv/
```
OR
```
conda activate venv
```

Install all the requirements in github repository
```
pip install -r requirements.txt
```


To add Files to git
```
git add.
```


OR
```
git add <file_name>
```

> NOTE: To ignore File or Folder from git we can write name of file/folder in .gitignore file

To Check the GIT Staus 
```
git status
```
To check al version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send changes to version/github
```
git push origin main
```

To check remote url
```
git remote -v
```

To setup the CI/CD Pipeline in heroku we need 3 information

1. HEROKU_EMAIL = vs.manikanta23@gmail.com
2. HEROKU_API_KEY = 104da8a1-0f77-49e6-a44f-3425cb71e92a
3. HEROKU_APP_NAME = ml-regresion-app


BUILD DOCKER IMAGE
```
docker build -t <image-name>:<tagname> .
```
> NOTE: image should be in lower case

To List docker image
```
docker image
```

Run Docker image
```
docker run -p 5000:5000 -e PORT=5000 4427633da66c
```

To check running Containers in docker
```
docker ps
```

To Stop any docker container
```
docker stop <container_id>
```


Create a folder housing in vs code (Folder should be empty in initial stage)
```
housing
```

create a new file 
```
setup.py
from setuptools import setup

from setuptools import setup
from typing import List
```


install kernel
```
pip install ipykernel
```

```
--- Create these objects in Entity:-  ----

DataIngestionConfig
DataValidationConfig
DataTransformationConfig
DataTrainerConfig
DataEvaluationConfig
ModelPusherConfig
```

```
create config.yaml in machine_learning folder itself

Config.yaml reads the config information that is required for our project.
```


```
We have created entity and config.yaml 
Now write code for config folder (Utilize Entity and config.yaml file aswell & giving configuration to the pipeline)
```


```
create configuration.py file inside housing & inside config
```

```
From config.yaml file how can i read the information
Write code in example.ipynb 
```

```
Util is a kind of helper function & It is Used when it is required
create a util folder inside housing folder
create a file inside util folder called util.py

```

```
create a constant folder inside housing
```