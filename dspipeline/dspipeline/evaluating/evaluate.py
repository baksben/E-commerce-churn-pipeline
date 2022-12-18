'''Evaluate test data
'''
from sklearn.metrics import *
import pandas as pd

class Metric:

    def __init__(self):
        pass

    def accuracy(self, y_true, y_preds):
        '''Calculate accuracy score
        Args:
            y_true pandas.Series: true target values
            y_preds pandas.Series: predicted target values
        
        Returns:
            roc_auc float: accuracy score
        '''
        acc = accuracy_score(y_true, y_preds)

        return acc

    def recall(self, y_true, y_preds):
        '''Calculate recall
        Args:
            y_true pandas.Series: true target values
            y_preds pandas.Series: predicted target values
        
        Returns:
            rec float: recall score
        '''
        rec = recall_score(y_true, y_preds)

        return rec

    def precision(self, y_true, y_preds):
        '''Calculate precision score
        Args:
            y_true pandas.Series: true target values
            y_preds pandas.Series: predicted target values
        
        Returns:
            prec float: precision score
        '''
        prec = precision_score(y_true, y_preds)

        return prec

    def roc_auc(self, y_true, y_preds):
        '''Calculate ROC AUC score
        Args:
            y_true pandas.Series: true target values
            y_preds pandas.Series: predicted target values
        
        Returns:
            roc_auc float: ROC AUC score
        '''
        roc_auc = roc_auc_score(y_true, y_preds)

        return roc_auc

    def calculate_score(self, score_list, y_true, y_preds):
        '''Calculate scores
        Args:
            score_list list: list of scores
            y_true pandas.Series: true target values
            y_preds pandas.Series: predicted target values probability
        
        Returns:
            scores pandas.DataFrame
        '''

        score_dict = {'accuracy': self.accuracy, 'precision': self.precision, 'recall': self.recall, 'roc_auc': self.roc_auc}

        scores = pd.DataFrame()
        y_preds_c = (y_preds[:, 1]>0.5) * 1
        for score in score_list:
            if score != 'roc_auc':
                scores.loc[0, score] = score_dict[score](y_true, y_preds_c)
            else:
                scores.loc[0, score] = score_dict[score](y_true, y_preds[:, 1])

        return scores