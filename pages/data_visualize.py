import streamlit as st
import pandas as pd
import matplotlib as mp
import plotly.express as fancyplot

import dbfunc as estate

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


# -------- Scatterplot and Heatmap --------


if st.button("Advanced Graphs"):

    fig = fancyplot.density_heatmap(data, x="location", y="property_type", z="price", 
                            hover_data=["name", "area_sqft"], color_continuous_scale="Viridis")

    fig.update_layout(title="Price Heatmap by Location and Property Type",
                    xaxis_title="Location",
                    yaxis_title="Property Type")

    st.plotly_chart(fig)

    fig = fancyplot.scatter(data, x='area_sqft', y='price', color='location',
                 title='Price vs Area for Different Properties',
                 labels={'area_sqft': 'Area (sq ft)', 'price': 'Price (in ₹)', 'location': 'Location'})
    
    st.plotly_chart(fig)

