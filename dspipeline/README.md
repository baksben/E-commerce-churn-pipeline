# homework-6-computing-data-science


### hw6.py
Python file with solution for each task

### diabetesoop python package 

#### folder structure

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   │
│   └── sample_diabetes_mellitus_data.csv            <- Input datadump.
│
│
├── notebooks          <- Jupyter notebooks testing the diabetes package (hm6_testing.ipynb)
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── diabetesoop                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           
│   │   │
│   │   └── load.py    <- Read data
│   │
│   │
│   ├── processing     <- Scripts to process data (remove nas, dummify, split into train andt test)
│   │   │ 
│   │   ├── transformer.py   <- Scripts to dummify 
│   │   └── prep.py <- Scripts to deal with NaNs
│   │
│   │
│   └── modeling       <- Scripts to train model and predict
│       └── model.py   <- Scripts to train model and predict
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```
