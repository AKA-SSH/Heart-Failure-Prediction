import os
import sys
import dill

import numpy as np
import pandas as pd
from tabulate import tabulate

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from src.logger import logging
from src.exception import CustomException


def save_object(file_path, obj):
    '''
    This function saves object as a pickle file

    Input:
        - File Path
        - Object
    
    Output:
        - Pickle File
    '''
    try:
        dir_path= os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok= True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    
    except Exception as CE:
        logging.error(f'error during object saving: {str(CE)}', exc_info= True)
        raise CustomException(CE, sys)

def evaluate_model(true, pred):
    '''
    This function returns an evaluation table with accuracy, precision, recall and F1 score

    Input:
        - True Value
        - Predicted Value
    
    Output:
        - Evaluation Table
    '''
    ACC= accuracy_score(true, pred)
    PRE= precision_score(true, pred)
    REC= recall_score(true, pred)
    F1= f1_score(true, pred)
    table= [['ACC:', ACC],
            ['PRE:', PRE],
            ['REC:', REC],
            ['F1:', F1]]
    
    evaluation= tabulate(table, headers= ['METRIC', 'SCORE'], tablefmt= 'grid')
    return evaluation