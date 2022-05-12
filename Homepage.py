import pandas as pd
import streamlit as st
from PIL import Image





#### Page Title ####
def app():
    st.title("📊Supermarket Sales Analysist📊")
    img = Image.open('supermarket.jpg')
    st.image(img,use_column_width=True, caption='Supermarket Illustration')

    #### Introduction ####
    st.markdown("""
   ---
    Introduction:
    - **Name** : Rahmat Fadhli Syauqi
    - **Batch**: FTDS Batch 11
    ---
    """)


    #### Columns Directory ####
    st.header('Table of Contents')
    st.markdown("""
    ---
        This analysist contain 2 chapter that we will presenting \
        from the dataset of supermarket sales at Myanmar, \
        first chapter is Vissualization, and the second part is \
        Hypotesist Test.
        ---
    """)


    #Columns with notation
    col1, col2= st.columns(2)

    with col1:
        st.subheader('Data Visualization')
        st.image('Graph_city.png')
        st.markdown("""
        Data visualization is the graphical representation of information \
        and data. On this chapter i will introduct the analysist \
        with the graph that we can easy understand and reminding, \
        included bar chart and line chart.
        
        """)
    with col2:
        st.subheader('Hypotesist Test')
        st.image('hypo_test.png')
        st.markdown("""
        Hypothesis testing is an act in statistics whereby an analyst tests 
        an assumption regarding a population parameter. \
        The methodology employed by the analyst depends on the nature \
        of the data used and the reason for the analysis. \
        In this case study, we use average purchase from\
        Male customer type and Female customer type of SuperMarket Sales  
        Datasets.
        
        """)




