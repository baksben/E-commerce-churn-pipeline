'''Split data into train and test
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from dspipeline.data.load import Data

class Split():

    def __init__(self):
        pass

    def split_train_test(self, data, target):
        '''Split data

        Args:
            data (pandas.DataFrame): dataframe
            target (str): name of target variable
        
        Returns:
            X_y_train, X_y_test (pd.DataFrame): train and test dataframes
        '''
        # define feature set X and traget variable y
        if target not in data.columns:
            raise Exception(f'{target} column not in the dataframe!! Please choose target variable as a column present in the dataframe!!')

        X, y = data.drop(columns=[target]), data[target]

        # divide into training and testing sets for features and target variables
        X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

        # join features and target columns per specification
        X_y_train = X_train.join(pd.DataFrame({target: y_train}))
        X_y_test = X_test.join(pd.DataFrame({target: y_test}))
        
        return X_y_train, X_y_test

    def split_cross_val(self, data, target, n_folds):
        '''Split data cross validation

        Args:
            data (pandas.DataFrame): dataframe
            target (str): name of target variable
            n_folds (int): number of folds
        
        Returns:
            list X_y_train, X_y_test (pd.DataFrame): train and test dataframes
        '''
        # define feature set X and traget variable y
        if target not in data.columns:
            raise Exception(f'{target} column not in the dataframe!! Please choose target variable as a column present in the dataframe!!')

        X, y = data.drop(columns=[target]), data[target]

        # define kfolds objects
        kf = KFold(n_splits=n_folds, shuffle=False)

        # define empty output objects lists to hold train and evaluation data
        train_list = []
        eval_list = []


        for train_index, eval_index in kf.split(X.index):
            train_list.append([X.iloc[train_index,:], y.iloc[train_index]])
            eval_list.append([X.iloc[eval_index,:], y.iloc[eval_index]])
        
        return train_list, eval_list