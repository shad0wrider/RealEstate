import streamlit as st

import real_estate_appv2 as estate

import folium as failed
import api , json
from streamlit.components.v1 import html


st.subheader("Add New Estate")
name = st.text_input("Estate Name")
location = st.text_input("Location")
price = st.number_input("Price (₹)", min_value=0.0, step=1000.0)
area = st.number_input("Area (sqft)", min_value=0.0)
ptype = st.selectbox("Estate Type", ["Flat", "Villa", "Plot", "Other"])



# Render the map in Streamlit using the HTML component

if st.button("Show Location On Map"):
    if len(location) == 0:
        st.warning("Address of Estate cannot be empty")
    
    else:
        get_latlong = api.get_location(location)
        if get_latlong:
            latitude = get_latlong[0]["lat"]
            longitude = get_latlong[0]["lon"]
            place_name = get_latlong[0]["display_name"]

            m = failed.Map(location=[latitude,longitude], zoom_start=23)
            failed.Marker([longitude,latitude], popup=place_name).add_to(m)
            html_string = m._repr_html_()  # Get the HTML representation of the map
            html(html_string, height=500)

        elif get_latlong == "Error" or "Not Found":
            st.warning("Location not found :(")

if st.button("Add Estate"):
    estate.add_estate(name, location, price, area, ptype)
    st.success("✅ Estate added successfully!")
