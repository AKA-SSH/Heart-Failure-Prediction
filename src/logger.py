# library
import os
import logging
from datetime import datetime

# creating log directory
log_path= os.path.join(os.getcwd(), 'logs')
os.makedirs(log_path, exist_ok= True)

# naming the log entry
log_file= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
log_file_path= os.path.join(log_path, log_file)

# setting log level
log_level= logging.INFO

# log message
logging.basicConfig(filename= log_file_path,
                    format= '%(asctime)s [%(levelname)s] %(name)s - %(message)s',
                    level= log_level)