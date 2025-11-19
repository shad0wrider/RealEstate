import streamlit as st

import real_estate_appv2 as estate

st.subheader("Delete Estate")
pid = st.number_input("Enter Estate ID to Delete",min_value=0)
if st.button("Delete"):
    if_done = estate.delete_estate(pid)
    if if_done == "Done":
        st.success("🗑️ Estate deleted successfully!")
    elif if_done == "Error":
        st.warning("Estate ID not found :(")
