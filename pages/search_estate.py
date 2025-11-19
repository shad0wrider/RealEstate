import streamlit as st

import real_estate_appv2 as estate

st.subheader("Search Estate by ID")
pid = st.number_input("Enter Estate ID", min_value=1, step=1)
if st.button("Search"):
    data = estate.get_estate_by_id(pid)
    if data.empty:
        st.error("❌ No Estate found with that ID.")
    else:
        st.dataframe(data)
