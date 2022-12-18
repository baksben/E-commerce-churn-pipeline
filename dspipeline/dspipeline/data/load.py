'''Load the data
'''
import pandas as pd

class Data:

    def __init__(self, filename, tab_alias=None):
        self.filename = filename
        self.tab_alias = tab_alias

    def from_csv(self):
        '''Reads data from csv

        Args:
            filename (str): filename and path of data
            target (str): name of target variable
        
        Returns:
            data (pd.DataFrame): input dataframes
        '''
        try:
            data = pd.read_csv(self.filename, index_col=0)

            return data

        except FileNotFoundError:
            raise Exception ('Please specify path and filename correctly!!!')

    def from_excel(self):
        '''Reads data from excel

        Args:
            filename (str): filename and path of data
            target (str): name of target variable
            tab_alias (str): alias of a tab
        
        Returns:
            data (pd.DataFrame): input dataframes
        '''
        try:
            data = pd.read_excel(self.filename, index_col=0, sheet_name=self.tab_alias)
            
            return data

        except FileNotFoundError:
            raise Exception ('Please specify path and filename correctly!!!')


