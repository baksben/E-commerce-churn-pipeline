'''Deal with NA data points
'''

class Preprocessor:

    def __init__(self, data):
        self.data = data

class DropNaNs(Preprocessor):

    def __init__(self, data, columns_l):
        super().__init__(data)
        self.columns_l = columns_l

    def drop(self):
        '''Drop nas from a dataframe

        Args:
            self
            
        Return:
            proc_data pd.DataFrame: processed dataframe
        '''
        try:
            proc_data = self.data.dropna(subset=self.columns_l)
            return proc_data

        except KeyError:
            raise Exception ('Please make sure columns exist in your data!!')


class FillNaNs(Preprocessor):

    def __init__(self, data, columns_l):
        super().__init__(data)
        self.columns_l = columns_l

    def fill(self):
        '''Fill nas from a dataframe

        Args:
            self
        
        Return:
            proc_data pd.DataFrame: processed dataframe
        '''
        try:
            proc_data = self.data.fillna(value=self.data[self.columns_l].mean())
            return proc_data

        except KeyError:
            raise Exception ('Please make sure columns exist in your data!!')