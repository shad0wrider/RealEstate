import streamlit as st
import sqlite3 as sql
import pandas as pd

# ---------- Database Connection ----------
def get_connection():
    return sql.connect("db.db")

# ---------- Database Functions ----------
def add_estate(name, location, price, area, ptype):
    con = get_connection()
    cur = con.cursor()
    query = "INSERT INTO properties (id , name, location, price, area_sqft, property_type) VALUES (?, ?, ?, ?, ?, ?)"
    tmp = cur.execute("SELECT * from properties")
    id_plus_one = len(tmp.fetchall())+1
    cur.execute(query, (id_plus_one , name, location, price, area, ptype))
    con.commit()
    con.close()

def view_estates():
    con = get_connection()
    df = pd.read_sql("SELECT * FROM properties", con)
    con.close()
    return df

def get_estate_by_id(pid):
    con = get_connection()
    df = pd.read_sql(f"SELECT * FROM properties WHERE id={pid}", con)
    con.close()
    return df

def get_all_estates():
    con = get_connection()
    data = pd.read_sql(f"SELECT * from properties",con)
    con.close()
    return data

def update_estate(pid, price, area):
    con = get_connection()
    cur = con.cursor()
    cur.execute("UPDATE properties SET price=?, area_sqft=? WHERE id=?", (price, area, pid))
    con.commit()
    con.close()

def delete_estate(pid):
    con = get_connection()
    cur = con.cursor()
    try:
        tmp = cur.execute(f"SELECT * FROM properties where id={pid}")
        tmpdata = cur.fetchall()
        if tmpdata != []:
            cur.execute("DELETE FROM properties WHERE id=?", (pid,))
            con.commit()
            con.close()
            return "Done"
        else:
            return "Error"
    except Exception as ie:
        print(ie)
        return "Error"

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
