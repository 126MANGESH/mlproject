import os
import sys
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str  = os.path.join('artifacts', 'test.csv')
    raw_data_path: str   = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entering data ingestion method")
        try:
            # Verify this path exists (note: 'notbook' might be 'notebook' in your repo)
            src_csv = r'D:\ML_project_krish\ml_project\notbook\stud.csv'
            df = pd.read_csv(src_csv)
            logging.info('Dataset read as pandas DataFrame')

            # Create artifacts folder
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)

            # Save raw/full copy
            df.to_csv(self.config.raw_data_path, index=False, header=True)

            # Split and save
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)
            logging.info("Ingestion completed: raw, train, and test saved")

            return (
                self.config.train_data_path,
                self.config.test_data_path,
                self.config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data, raw_data = obj.initiate_data_ingestion()

    transformer = DataTransformation()
    data_transformation = transformer.initiate_data_transformation(train_data, test_data)
