import streamlit as st
import pandas as pd
import matplotlib as mp
import numpy as np

import real_estate_appv2 as estate

dataframe = pd.DataFrame(estate.get_all_estates())

print(dataframe)