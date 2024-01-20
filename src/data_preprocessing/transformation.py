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
            N_pipeline= Pipeline(steps= ('scaler', MinMaxScaler()))
            logging.info('numeric pipeline created')

            # creating pipeline for categorical columns
            C_pipeline= Pipeline(steps= ('one_hot_encoder', OneHotEncoder()))
            logging.info('categoric pipeline created')

            # combining both pipelines
            preprocessor= ColumnTransformer(transformers= [('numeric pipeline', N_pipeline, N_columns),
                                                           ('categoric pipeline', C_pipeline, C_columns)])
            logging.info('pipeline creation completed')
            return preprocessor

        except Exception as CE:
            logging.error(f'error during data ingestion: {str(CE)}', exc_info= True)
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
            pass

        except:
            pass