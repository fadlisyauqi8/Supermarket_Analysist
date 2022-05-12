import streamlit as st
import Homepage,eda,Hypotest
import pandas as pd



######### Set Page Config #########
st.set_page_config(
    page_title="Supermarket Sales Analysist",
    page_icon="🏪",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/fadlisyauqi8',
        'Report a bug': "https://www.google.com/",
        'About': "# The apps that you need to analyze sales of supermarket at Myanmar!"
    }
)


PAGES = {'Homepage' : Homepage,
        'Data Visualization': eda,
        'Hypothesis Testing': Hypotest}


st.sidebar.title("Navigation")
selected = st.sidebar.selectbox('Please Select Page:', options= PAGES.keys())
page = PAGES[selected]
page.app()
