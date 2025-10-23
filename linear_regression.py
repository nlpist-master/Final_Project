# steps:
# 1. create a process of inserting data, train and predict
# 2. Change data from array to CSV
# 3. Pack all the process into a function and call it + send parameters
# AS SIMPLEST AS POSSIBLE

# import logging module to track all the steps of the process
import logging

# setup minimal log level to display
logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s: %(message)s',
    datefmt='%d/%m/%Y - %H:%M:%S'
    )


def load_modules_with_logs() -> tuple:
    """
    load heavy modules with progress log, so the user can track the process steps
    return the modules
    """
    logging.info('import numpy as np...')
    import numpy as np
    logging.info("import matplotlib.pyplot as plt...")
    import matplotlib.pyplot as plt
    logging.info("from sklearn.linear_model import LinearRegression...")
    from sklearn.linear_model import LinearRegression

    return np, plt, LinearRegression


if __name__ == '__main__':
    np, plt, LinearRegression = load_modules_with_logs()
    # data
    work_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # work hours per day
    print(work_hours.shape)
