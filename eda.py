import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import numpy as np


def app():
        #### Title Viz Page ####
        st.title('Supermarket Sales Analysist Vissualization')

        st.markdown("""
        This app performs Supermarket sales stats data!
        * **Library:** pandas, streamlit
        * **Data source:** (https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales)

        """)
        #### Loading Data ####
        @st.cache
        def load_data(nrows):
                df = pd.read_csv('cleanData.csv',nrows=nrows)
                lowercase = lambda x: str(x).lower()
                df.rename(lowercase, axis='columns', inplace=True)
                return df

        data_load_state = st.text('Loading data...')
        df = load_data(10000)
        data_load_state.text("Done! (using st.cache)")

        #### Raw Data ####
        st.subheader('Raw Data')
        if st.checkbox('Show raw data'):
                st.write('This is dataset that we use to analyze')
                st.write(df)

                st.markdown(
                ''' <h3>
                Shown are Insights the Visualization of the dataset</h3>''', unsafe_allow_html=True)

                #### Widget ####
                with st.expander('Revenue by Product Sales'):
                        column1, column2 = st.columns([3,1])
                        df = pd.read_csv('cleanData.csv')
                        df['date']=  pd.to_datetime(df['date'], format = '%Y-%m-%d').dt.date
                        date_min = df["date"].min()
                        date_max = df["date"].max()
                                #
                        date_slider = column1.slider(label="Select Date",
                                                min_value = date_min,
                                                max_value = date_max,
                                                value = (date_min, date_max))
                        select_city = column2.selectbox('Select City', df.sort_values('City').City.unique(),key = "City")
                        df_select = df[ (df["date"] >= date_slider[0]) & 
                                        (df["date"] <= date_slider[1]) & (df["City"] == select_city) ]
                        a = df_select.groupby('product_line')['gross_income'].sum().sort_values(ascending=False).reset_index()
                        fig=px.bar(a, x='product_line', y='gross_income', color=a.product_line)
                        column3,column4=st.columns([3,2])
                        column3.plotly_chart(fig)
                        st.write(f'In {select_city}  at {date_slider[0]} until {date_slider[1]} \
                the most profitable product is {a.values[0,0]} with {a.values[0,1]} gross income')


                with st.expander('Productivity of the Branch'):
                        col1, col2 = st.columns([3,1])
                        values = col1.slider('Time Operating', int(df.time.min()), int(df.time.max()), step=1)
                        select_branch=col2.selectbox('Select Branch',df.sort_values("branch").branch.unique())  
                        count = df[(df["City"] == select_city) & ( df.time == values)].quantity.sum()
                        st.write(f'Productivity in branch {select_branch} at {values}  O`clock, {count} of product sold ') 

                with st.expander('City Gross Income '):
                        city_income=px.histogram(df.sort_values('City') ,x='City', y='gross_income', color = 'City',)
                        gross_income = df.groupby(['City'])['gross_income'].sum()
                        gross_income_max = gross_income.sort_values(ascending=False).reset_index()
                        st.plotly_chart(city_income, use_container_width=True)   
                        st.write((f'The city that have highest gross income is city {gross_income_max.values[0,0]} by {gross_income_max.values[0,1]} of gross income'))

                with st.expander('Favorite product by Gender within city'):
                        column1, column2 = st.columns([3,1])
                        #Variables 
                        #male_product = df[df['gender'] == 'Male'].groupby(['product_line','gender']).count()['quantity'].sort_values(ascending=False).reset_index()
                        #female_product = df[df['gender'] == 'Female'].groupby(['product_line','gender']).count()['quantity'].sort_values(ascending=False).reset_index()


                        #Callback
                        selected_gender = st.radio('What is your Gender:', ['Male', 'Female'], index = 0)
                        select_city = column2.selectbox('Select City',df.sort_values('City').City.unique())
                        df_select_gender = df[ (df["gender"] == selected_gender) & (df["City"] == select_city) ]
                        b = df_select_gender.groupby('product_line')['gross_income'].sum().sort_values(ascending=False).reset_index()
                        fig=px.bar(b, x='product_line', y='gross_income', color=a.product_line)
                        column3,column4=st.columns([3,2])
                        column3.plotly_chart(fig)
                        st.write(f'What {selected_gender} most buy in city {select_city} most buy product is {b.values[0,0]} with {b.values[0,1]} gross income  ') 

                        


                                




