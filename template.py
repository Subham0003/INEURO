import os
from pathlib import Path

list_of_files=[
    ".github/workflows.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_training.py",
    "src/components/model_evaluation.py",
    "src/Pipeline/__init__.py",
    "src/Pipeline/data_pipeline.py",
    "src/Pipeline/training_pipeline.py",
    "src/Pipeline/prediction_pipeline.py",
    "src/logger/logging.py",
    "src/utils/utils.py",
    "src/utils/__init__.py",
    "src/exception/exception.py",
    "test/unit/__init__.py",
    "test/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt"
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox/ini",
    "experiment/experiment.ipynb"

]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file