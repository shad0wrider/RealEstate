# import streamlit as st
import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plot
import plotly.express as fancyplot

file = sql.connect("db.db")

data = pd.read_sql("SELECT * from properties",file)

cities = data["location"].unique()

# selector = st.selectbox("Select City",cities)

cities = data["location"].unique()

all_price = data.groupby("location")["price"].value_counts()

all_feet = data.groupby("location")["area_sqft"].value_counts()


fig = plot.bar(all_price,all_feet)

plot.show()