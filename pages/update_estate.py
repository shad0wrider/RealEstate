import streamlit as st

import real_estate_appv2 as estate

st.subheader("Update Estate Details")
pid = st.number_input("Enter Estate ID to Update", min_value=1, step=1)
new_price = st.number_input("New Price (₹)", min_value=0.0, step=1000.0)
new_area = st.number_input("New Area (sqft)", min_value=0.0)
if st.button("Update"):
    estate.update_estate(pid, new_price, new_area)
    st.success("✅ Estate updated successfully!")
