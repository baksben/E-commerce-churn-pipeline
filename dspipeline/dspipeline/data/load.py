'''Load the data
'''
import pandas as pd
from sklearn.model_selection import train_test_split

class Data:

    def __init__(self):
        pass

    def split_treain_test(self, data: pd.DataFrame, target: str):
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

    def from_csv(self, filename: str, target: str):
        '''Reads data from csv

        Args:
            filename (str): filename and path of data
            target (str): name of target variable
        
        Returns:
            X_y_train, X_y_test (pd.DataFrame): train and test dataframes
        '''
        try:
            data = pd.read_csv(filename, index_col=0)

            X_y_train, X_y_test = self.split_treain_test(data, target)

            return X_y_train, X_y_test

        except FileNotFoundError:
            raise Exception ('Please specify path and filename correctly!!!')

    def from_excel(self, filename: str, target: str, tab_alias: str):
        '''Reads data from excel

        Args:
            filename (str): filename and path of data
            target (str): name of target variable
            tab_alias (str): alias of a tab
        
        Returns:
            X_y_train, X_y_test (pd.DataFrame): train and test dataframes
        '''
        try:
            data = pd.read_excel(filename, index_col=0, sheet_name=tab_alias)

            X_y_train, X_y_test = self.split_treain_test(data, target)

            return X_y_train, X_y_test

        except FileNotFoundError:
            raise Exception ('Please specify path and filename correctly!!!')


