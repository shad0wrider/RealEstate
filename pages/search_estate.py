import streamlit as st

import dbfunc as estate

st.subheader("Search Estate by Name")
name = st.text_input("Enter Estate Name")
if st.button("Search"):
    data = estate.get_estate_by_name(name)
    if data.empty:
        st.error("❌ No Estate found with that Name.")
    else:
        st.dataframe(data)
