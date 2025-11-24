import streamlit as st
import sqlite3 as sql
import pandas as pd


# ---------- Streamlit Frontend ----------
st.set_page_config(page_title="🏠 Real Estate Management System", layout="centered")

st.title("🏠 Real Estate Management System")
# menus = ["Add Property", "View Properties", "Search Property", "Update Property", "Delete Property"]
# choice = st.sidebar.radio("Navigation", menus )

# page1,page2,page3,page4,page5 = st.columns(5)

home = st.Page("pages/home.py",title="About Project")

visualize = st.Page("pages/data_visualize.py",title="Visualize Data")

# ----------- Add Property -----------
page1 =st.Page("pages/add_estate.py",title="Add New Estate")
# ----------- View Properties -----------
page2 =st.Page("pages/view_estate.py",title="View Locations")

# ----------- Search Property -----------
page3 =st.Page("pages/search_estate.py",title="Search Estates")

# ----------- Update Property -----------
page4 =st.Page("pages/update_estate.py",title="Update Estates")

# ----------- Delete Property -----------
page5 =st.Page("pages/delete_estate.py",title="Delete Estate")

mainpage = st.navigation([home,page1,page2,page3,page4,page5,visualize])

mainpage.run()
