import streamlit as st

import dbfunc as estate

st.subheader("All Estates")
df = estate.view_estates()
st.dataframe(df, use_container_width=True)
