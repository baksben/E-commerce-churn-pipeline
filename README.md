# homework-final-computing-data-science

### dspipeline python package

#### folder structure

```
├── LICENSE
├── README.md          <- The top-level README for developers using this project.
├── data
│   │
│   └── E Commerce Dataset.xlsx        <- Input datadump.
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
│   ├── splitting
│   │   │
│   │   └── split.py    <- SPlit data into train test/Cross validation
│   │
│   │
│   ├── processing     <- Scripts to process data (remove nas, dummify, split into train andt test)
│   │   │
│   │   ├── transformer.py   <- Scripts to dummify, binarize, log
│   │   └── prep.py <- Scripts to deal with NaNs
│   ├── evaluating     <- Scripts to evaluate model
│   │   │
│   │   └── evaluate.py <- Scripts to evaluate with different scores
│   │
│   └── modeling       <- Scripts to train model and predict
│       └── model.py   <- Scripts to train model and predict
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

### How to work & develop the package?

#### Preprocessors

There is parent class Preprocessor from which developer needs to inherit for a new subclass. Methods should be called according to functionality of subclass.

#### Feature Generator

There is parent meta class Transformer from which developer needs to inherit for a new subclass. There is uniform method of generate that developer should create with functionality that subclass represents.

#### Models

There is Model class which serves as a wrapper around scikit-learn models. Currently Logistic Regression and Random Forest algorithm is supported. There are 3 methods: train, predict and predict proba. Train stands for training data, predict responsible for returning prediction as classes i.e. 1/0, predict proba returns probailities for each class.

#### Evaluation

There is Metric class with various methods for each metrics. To develop new one developer should create relevant function add it to calculate_score method's score_dict object with key and value as reference pointer to the function. Also must specify in if else part whether it uses preicted probabilities or class to calculate metric.
