import sys
import time

# הודעת פתיחה לפני טעינת הספריות
def spinning_loader(message: str = "Initializing", duration: float = 3.0):
    spinner = ['|', '/', '-', '\\']
    sys.stdout.write(f"{message}... ")
    sys.stdout.flush()
    t_end = time.time() + duration
    i = 0
    while time.time() < t_end:
        sys.stdout.write(spinner[i % len(spinner)])
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
        i += 1
    sys.stdout.write("Done!\n")


# הפעלת האנימציה לפני ה־imports
spinning_loader("Loading modules, please wait")

# רשימת ה־imports בראש הקובץ – לפי הקונבנציה התקנית
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("✅ All modules loaded successfully.")
