import streamlit as st
from modules.method_selection import show_method_selection
from modules.runoff_output import show_runoff_output

st.set_page_config(page_title="💧 HydroFlow App", layout="wide")

st.sidebar.title("🌦️ HydroFlow Runoff Calculator")
page = st.sidebar.radio("Navigate", ["Method Selection", "Runoff Output"])

if page == "Method Selection":
    show_method_selection()
elif page == "Runoff Output":
    show_runoff_output()
