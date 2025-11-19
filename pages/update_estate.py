import streamlit as st

import real_estate_appv2 as estate

st.subheader("Update Estate Details")
pid = st.text_input("Enter Estate ID to Update")
new_price = st.number_input("New Price (₹)", min_value=0.0, step=1000.0)
new_area = st.number_input("New Area (sqft)", min_value=0.0)
if st.button("Update"):
    if len(pid) == 0:
        st.error("Estate ID cannot be empty ")
    estate.update_estate(int(pid), new_price, new_area)
    st.success("✅ Estate updated successfully!")
