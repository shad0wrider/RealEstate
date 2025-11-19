import streamlit as st

import real_estate_appv2 as estate

st.subheader("All Estates")
df = estate.view_estates()
st.dataframe(df, use_container_width=True)
