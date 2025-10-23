import sys
import time

# הודעת פתיחה לפני טעינת הספריות
def show_loading_bar(message: str = "Initializing system", duration: float = 3.0, steps: int = 30):
    """Show a simple progress bar before loading heavy modules."""
    sys.stdout.write(f"{message}... ")
    sys.stdout.flush()

    for i in range(steps):
        time.sleep(duration / steps)
        sys.stdout.write("█")
        sys.stdout.flush()
    sys.stdout.write(" Done!\n")

# הפעלת האנימציה לפני ה־imports
show_loading_bar("Loading modules, please wait")

# רשימת ה־imports בראש הקובץ – לפי הקונבנציה התקנית
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("✅ All modules loaded successfully.")
