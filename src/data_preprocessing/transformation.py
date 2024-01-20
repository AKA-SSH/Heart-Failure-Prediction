# import required libraries
import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

from src.utils import *
from src.logger import logging
from src.exception import CustomException

# data transformation program
@dataclass
class DataTransformationConfiguration:
    preprocessor_object_file_path= os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_configuration= DataTransformationConfiguration()
    
    def create_data_transformation_object(self):
        '''
        This function creates data transformation preprocessor

        Input:
            - Numerical Columns
            - Categorical Columns
        
        Output:
            - Preprocessor Object
        '''
        try:
            # listing down numerical and categorical columns
            N_columns= ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
            C_columns= ['Sex', 'ChestPainType', 'FastingBS', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

            # creating pipeline for numerical columns
            logging.info('pipeline creation initiated')
            N_pipeline= Pipeline(steps= [('scaler', MinMaxScaler())])
            logging.info('numeric pipeline created')

            # creating pipeline for categorical columns
            C_pipeline= Pipeline(steps= [('one_hot_encoder', OneHotEncoder())])
            logging.info('categoric pipeline created')

            # combining both pipelines
            preprocessor= ColumnTransformer(transformers= [('numeric pipeline', N_pipeline, N_columns),
                                                           ('categoric pipeline', C_pipeline, C_columns)])
            logging.info('pipeline creation completed')
            return preprocessor

        except Exception as CE:
            logging.error(f'error during preprocessor object creation: {str(CE)}', exc_info= True)
            raise CustomException(CE, sys)
    
    def initiate_data_transformation(self, train_data_file_path, test_data_file_path):
        '''
        This function performs data transformation

        Input:
            - Training Data
            - Testing Data
        
        Output:
            - Transformed Training Data
            - Transformed Testing Data
        '''
        try:
            # loading data
            logging.info('data transformation initiated')
            logging.info('loading train and test data')
            train_dataframe= pd.read_csv(train_data_file_path)
            test_dataframe= pd.read_csv(test_data_file_path)
            logging.info('loading completed')

            # creating preprocessor object
            logging.info('preprocessor creation initiated')
            preprocessor_object= self.create_data_transformation_object()
            logging.info('preprocessor creation completed')
            
            target= 'HeartDisease'

            # training data separation
            train_features= train_dataframe.drop(target, axis= 1)
            train_target= train_dataframe[target]
            logging.info('train features and target separated')

            # testing data separation
            test_features= test_dataframe.drop(target, axis= 1)
            test_target= test_dataframe[target]
            logging.info('test features and target separated')

            # using preprocessor object to data
            logging.info('preprocessor training on training data')
            transformed_train_features= preprocessor_object.fit_transform(train_features)
            logging.info('transformation of training data completed')
            transformed_test_features= preprocessor_object.transform(test_features)
            logging.info('transformation of testing data completed')

            # saving transformed data
            transformed_train_data= np.c_[transformed_train_features, np.array(train_target)]
            transformed_test_data= np.c_[transformed_test_features, np.array(test_target)]
            logging.info('data transformation completed')

            save_object(file_path= self.data_transformation_configuration.preprocessor_object_file_path,
                        obj= preprocessor_object)
            logging.info(f'data transformer object saved to: {self.data_transformation_configuration.preprocessor_object_file_path}')
            
            return (transformed_train_data,
                    transformed_test_data, 
                    self.data_transformation_configuration.preprocessor_object_file_path)

        except Exception as CE:
            logging.error(f'error during data transformation: {str(CE)}', exc_info= True)
            raise CustomException(CE, sys)