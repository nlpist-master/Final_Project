# steps:
# 1. create a process of inserting data, train and predict
# 2. Change data from array to CSV
# 3. Pack all the process into a function and call it + send parameters
# AS SIMPLEST AS POSSIBLE


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import logging

# setup minimal log level to display
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s: %(message)s',
    datefmt='%d/%m/%Y - %H:%M:%S'
    )

logging.info('All modules loaded successfully')


# data
work_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # work hours per day
print(work_hours.shape)
