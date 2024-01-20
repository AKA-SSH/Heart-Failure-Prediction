# import required libraries
import os
import sys
from src.logger import logging
from src.exception import CustomException

import numpy as np
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

# data ingestion program
@dataclass
class DataIngestionConfiguration:
    train_data_file_path: str= os.path.join('artifacts', 'train_data.csv')
    test_data_file_path: str= os.path.join('artifacts', 'test_data.csv')
    raw_data_file_path: str= os.path.join('artifacts', 'raw_data.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_configuration= DataIngestionConfiguration()
    
    def initiate_data_ingestion(self, csv_file_path= 'data\heart_failure_prediction_dataset.csv'):
        try:
            logging.info('data ingestion initiated')

            # read CSV file
            dataframe= pd.read_csv(csv_file_path)
            logging.info('converted dataset into dataframe')

            # creating new directory if not already present
            os.makedirs(os.path.dirname(self.data_ingestion_configuration.train_data_file_path), exist_ok= True)
            logging.info(f'directory {os.path.dirname(self.data_ingestion_configuration.train_data_file_path)} created/touched')

            # transporting raw data to raw_data_file_path
            dataframe.to_csv(self.data_ingestion_configuration.raw_data_file_path,
                             header= True,
                             index= False)
            logging.info(f'raw data saved to: {self.data_ingestion_configuration.raw_data_file_path}')

            # handling data integrity issues
            logging.info('data handling initiated')
            
            # handling RestingBP
            Q1= np.percentile(dataframe.RestingBP, 25)
            Q3= np.percentile(dataframe.RestingBP, 75)
            IQR= Q3-Q1
            LB= Q1 - 1.5*IQR
            dataframe.RestingBP= list(map(lambda x: LB if x < LB else x, dataframe.RestingBP))

            # handling Cholesterol
            heart_patient_cholesterol= dataframe[dataframe.HeartDisease == 1].Cholesterol
            heart_patient_cholesterol = [i for i in heart_patient_cholesterol if i>125]
            median_cholesterol= np.percentile(heart_patient_cholesterol, 50)
            dataframe.Cholesterol= list(map(lambda x: median_cholesterol if x < 125 else x, dataframe.Cholesterol))

            logging.info('data handling completed')

            # splitting the data into train-test data
            logging.info('train-test split initiated')
            train_dataset, test_dataset= train_test_split(dataframe, test_size= 0.2, random_state= 42)

            # transporting train data to train_data_file_path
            train_dataset.to_csv(self.data_ingestion_configuration.train_data_file_path,
                                 header= True,
                                 index= False)
            logging.info(f'train data saved to: {self.data_ingestion_configuration.train_data_file_path}')

            # transporting test data to test_data_file_path
            test_dataset.to_csv(self.data_ingestion_configuration.test_data_file_path,
                                header= True,
                                index= False)
            logging.info(f'test data saved to: {self.data_ingestion_configuration.test_data_file_path}')
            logging.info('data ingestion completed')

            return (self.data_ingestion_configuration.train_data_file_path,
                    self.data_ingestion_configuration.test_data_file_path)

        except Exception as CE:
            logging.error(f'error during data ingestion: {str(CE)}', exc_info= True)
            raise CustomException(CE, sys)
        
# program execution
if __name__ == '__main__':
    object= DataIngestion()
    train_dataset, test_dataset= object.initiate_data_ingestion()