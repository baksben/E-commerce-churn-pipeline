'''Train a model
'''
import pandas as pd

class Model:
    
    def __init__(self, feature_columns, target_column, model, hyperparamaterers):
        self._feature_columns = feature_columns
        self._target_column = target_column
        self.model = model
        self._hyperparamaterers = hyperparamaterers


    def train(self, train_data):
        '''Train a model

        Args:
            train_data pandas.DataFrame: training set of feature and target variables
        
        '''
        # set feature and target objects from train dataframe
        try:
            X_train = train_data[self._feature_columns]
            y_train = train_data[self._target_column]
        except KeyError:
            raise Exception('Please provide feature and target names of columns from training set provided!!!')

        # fit model
        try:
            self.model = self.model(**self._hyperparamaterers)
        except ValueError:
            raise Exception('Parameters provided are invalid please check documentation for the selected model!!')

        try:
            self.model.fit(X_train, y_train)
        except ValueError:
            raise Exception('Parameters provided are invalid please check documentation for the selected model!!')

        print('Model has been fitted on training dataset!!')


    def predict(self, dataframe):
        '''Train a model

        Args:
            dataframe (pd.DataFrame): input dataframe
        
        Returns:
            preds (np.array): results from predict_proba()
        '''
        # set feature and target objects from dataframe
        try:
            X_dataframe = dataframe[self._feature_columns]
            y_dataframe = dataframe[self._target_column]
        except KeyError:
            raise Exception('Please provide feature and target names of columns from dataframe provided!!!')

        # predict model
        return self.model.predict(X_dataframe)

    def predict_proba(self, dataframe):
        '''Train a model

        Args:
            dataframe (pd.DataFrame): input dataframe
        
        Returns:
            preds (np.array): results from predict_proba()
        '''
        # set feature and target objects from dataframe
        try:
            X_dataframe = dataframe[self._feature_columns]
            y_dataframe = dataframe[self._target_column]
        except KeyError:
            raise Exception('Please provide feature and target names of columns from dataframe provided!!!')

        # predict model
        return self.model.predict_proba(X_dataframe)
