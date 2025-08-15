import logging
import os
from datetime import datetime

# Define the log file name with a unique timestamp
LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory where logs will be stored
logs_dir = "logs"

# Create the full path for the logs directory
logs_path = os.path.join(os.getcwd(), logs_dir)

# Create the logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Create the full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE_NAME)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%m/%d/%Y %H:%M:%S'
)

if __name__ == "__main__":
    logging.info("Logging has been set up successfully started.")