import os
import sys
import dill

import numpy as np
import pandas as pd

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