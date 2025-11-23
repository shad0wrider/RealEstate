# import streamlit as st
import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plot
import plotly.express as fancyplot

file = sql.connect("db.db")

data = pd.read_sql("SELECT * from properties",file)

cities = data["location"].unique()

# selector = st.selectbox("Select City",cities)

price = data["price"]

feet = data["area_sqft"]

data["avg_price"] = price//feet


new = data.groupby("location")["avg_price"].mean()



plot.boxplot(new)