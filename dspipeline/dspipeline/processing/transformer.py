'''Dummify data points
'''
import pandas as pd
from abc import ABCMeta, abstractmethod


class Transformer(metaclass=ABCMeta):

    def __init__(self, data):
        self.data = data
    
    @abstractmethod
    def generate(self):
        return NotImplementedError   
    
         
class Dummifier(Transformer):

    def __init__(self, data, columns_l):
        super().__init__(data)
        self.columns_l = columns_l

    def generate(self):
        '''Generate dummies from a dataframe
        
        Args:
        
        Return:
            proc_data pd.DataFrame: processed dataframe
        '''
        try:
            proc_data = pd.get_dummies(data=self.data, columns=self.columns_l)
            return proc_data

        except KeyError:
            raise Exception ('Please make sure columns exist in your data!!')
    
         
class Binarizer(Transformer):

    def __init__(self, data, init_column_name, binarized_column_name):
        super().__init__(data)
        self.init_column_name = init_column_name
        self.binarized_column_name = binarized_column_name

    def generate(self):
        '''Generate binary variable
        
        Return:
            proc_data pd.DataFrame: processed dataframe
        '''
        try:
            proc_data = pd.get_dummies(data=self.data, columns=[self.init_column_name], drop_first=True)
            proc_data = proc_data.rename(columns={[col for col in proc_data.columns if f'{self.init_column_name}_' in col][0]: self.binarized_column_name})
            return proc_data
        except KeyError:
            raise Exception ('Please make sure columns exist in your data!!')       
