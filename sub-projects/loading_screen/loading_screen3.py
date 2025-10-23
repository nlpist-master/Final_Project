import streamlit as st
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# הצגת הודעת טעינה
with st.spinner('🚀 Loading modules... please wait...'):
    time.sleep(2)  # רק הדמיה של זמן טעינה

st.success('✅ All modules loaded successfully!')
