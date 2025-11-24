import streamlit as st
import pandas as pd
import matplotlib as mp
import plotly.express as fancyplot

import real_estate_appv2 as estate

data = estate.get_all_estates()

cities = data["location"].unique()

price = data["price"]

feet = data["area_sqft"]

data["avg_price"] = price//feet


new = data.groupby("location")["avg_price"].mean()


fig = fancyplot.bar(
    new.reset_index(),x="location",y="avg_price",labels={"location":"City","avg_price":"Price per sqft"},color="location",text="location")

st.plotly_chart(fig)

selector = st.selectbox("Select City",cities)

filtered = data[data["location"]== selector]

counter = filtered["property_type"].value_counts().reset_index()

counter.columns = ["property_type","count"]

fig = fancyplot.pie(counter,names="property_type",values="count")

st.plotly_chart(fig)