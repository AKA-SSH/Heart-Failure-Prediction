# importing required libraries
import os
import sys
from dataclasses import dataclass

from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from src.utils import *
from src.logger import logging
from src.exception import CustomException

# model training program
@dataclass
class ModelTrainerConfiguration:
    trained_model_file_path= os.path.join('artifacts', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_configuration= ModelTrainerConfiguration()
    
    def initiate_model_trainer(self, transformed_train_dataset, transformed_test_dataset):
        '''
        This function initiates and trains a CatBoostClassifier() object and predict test targets using it

        Input:
            - Transformed Train Dataset
            - Transformed Test Dataset

        Output:
            - Evaluation Table
        '''
        try:
            logging.info('model training initiated')

            logging.info('data splitting initiated')
            transformed_train_features, transformed_train_target= transformed_train_dataset[:,:-1], transformed_train_dataset[:,-1]
            transformed_test_features, transformed_test_target= transformed_test_dataset[:,:-1], transformed_test_dataset[:,-1]
            logging.info('data splitting completed')

            logging.info('model configuration initiated')
            hyperparameters= {'iterations': 140, 
                              'depth': 6, 
                              'learning_rate': 0.06103212591097244, 
                              'random_strength': 0.7146091182619464, 
                              'bagging_temperature': 0.7569038177960598, 
                              'border_count': 76, 
                              'l2_leaf_reg': 4.660597952852741}
            model= CatBoostClassifier(**hyperparameters, verbose= False)
            logging.info('model configuration completed')

            logging.info('model training initiated')
            model.fit(transformed_train_features, transformed_train_target)
            logging.info('model training completed')
            
            logging.info('model prediction initiated')
            test_predictions= model.predict(transformed_test_features)
            logging.info('model prediction completed')

            logging.info('model evaluation initiated')
            model_report= evaluate_model(transformed_test_target, test_predictions)
            logging.info('model evaluation completed')

            logging.info('model pickling initiated')
            save_object(file_path= self.model_trainer_configuration.trained_model_file_path,
                        obj= model)
            logging.info('model pickling completed')

            return model_report

        except Exception as CE:
            logging.error(f'error during model training: {str(CE)}', exc_info= True)
            raise CustomException(CE, sys)