import streamlit as st
import pandas as pd
import matplotlib as mp
import numpy as np

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.bar_chart(dataframe)

