import streamlit as st
import pandas as pd
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


def app():
    st.title('HYPOTHESIS TESTING')

    st.caption('In this Hypothesis Testing we will prove which city has most productivity and the highest profit based on the gross income and sales quantity of the overall product sold.')


    st.subheader('Theory of Hypothesis Testing')
    st.image('hypo_pict.jpg')
    #Dataframe
    df = pd.read_csv('cleanData.csv')
    with st.expander('Show Productivity in Cities'):
        #Variables 
        gross_income_graph= px.histogram(df.sort_values("City"), x='gross_income', y='quantity' ,color='City', barmode='group')
        total_Q = df.groupby(['City','gross_income'])['quantity'].sum()
        total_Q= total_Q.groupby("gross_income").mean().reset_index()
        gross_line_graph=gross_income_graph.add_trace(go.Scatter(x=total_Q.gross_income, y=total_Q['quantity'],line_color = 'yellow', name="Quantity"))
        
        #Plotting graph
        st.plotly_chart(gross_line_graph,use_container_width=True)
        Naypyitaw_profit= (df[df['City']=='Naypyitaw'][['gross_income','quantity']].groupby('gross_income').sum())   
        Yangon_profit= (df[df['City']=='Yangon'][['gross_income','quantity']].groupby('gross_income').sum())
        Mandalay_profit= (df[df['City']=='Mandalay'][['gross_income','quantity']].groupby('gross_income').sum())
    
        #Average profit 
        Naypyitaw_profit= (df[df['City']=='Naypyitaw'][['gross_income','quantity']].groupby('gross_income').sum())   
        Yangon_profit= (df[df['City']=='Yangon'][['gross_income','quantity']].groupby('gross_income').sum())
        Mandalay_profit= (df[df['City']=='Mandalay'][['gross_income','quantity']].groupby('gross_income').sum())
        st.write('The average of profit in City Naypyitaw is : ', Naypyitaw_profit.quantity.mean())
        st.write('The average of profit in City Yangon is : ',Yangon_profit.quantity.mean())
        st.write('The average of profit in City Mandalay is : ',Mandalay_profit.quantity.mean())

        st.write('City of Yangon and Mandalay have similar average profit from the sales, \
        so we want to analyze with hypotesist notation')


    st.subheader('Hypothesis Notation')
    if st.checkbox('Show hypotesis notation'):
            st.write('This is hypotesis notation we use to testing')
            st.write("""
    - Null Hypothesis : Mean value of Yangon City is relatively the same as Mean value of Mandalay City
    - Alt. Hypothesis: Mean value of Yangon City is relatively the same as Mean value of Mandalay City""")

    st.write('''
    ----
    The average profit from both the city Yangon and Mandalay slightly similar, so we need to to use T-Test 2 sample 2 tailed the hypotest.
    With the use of **95% confidence interval** (0.05 Critical Value), here are the results:
    ''', unsafe_allow_html = True)


    st.subheader('T - Test 2 sample 2 tailed the hypotest') 
    if st.checkbox('Show T- Test 2 sample 2 tailed the hypotest'):
        t_stat, p_val = stats.ttest_ind(Yangon_profit,Mandalay_profit)
        st.write(f'P-value: {p_val}, T stat : {t_stat}')
        st.write('With the use of 95 Confidence Interval (0.05), P value is higher than Critical Value')
    

    viz_hypo=st.checkbox('See Visualization')
    if viz_hypo:
        #Simulation
        Yangon_sales = np.random.normal(Yangon_profit.quantity.mean(),Yangon_profit.quantity.std(),80)
        Mandalay_sales = np.random.normal(Mandalay_profit.quantity.mean(),Mandalay_profit.quantity.std(),80)

        #Confidence Interval
        ci = stats.norm.interval(0.95, Yangon_profit.quantity.mean(), Yangon_profit.quantity.std())
        #Plotting
        fig =plt.figure(figsize=(16,5))
        sns.distplot(Yangon_sales, label='Average Sales pada kota Yangon',color='blue')
        sns.distplot(Mandalay_sales, label='Average Sales pada kota Mandalay',color='red')
        #Mean
        plt.axvline(Yangon_profit.quantity.mean(), color='blue', linewidth=2, label='Yangon mean')
        plt.axvline(Mandalay_profit.quantity.mean(), color='red',  linewidth=2, label='Mandalay mean')
        #Line
        plt.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
        plt.axvline(ci[0], color='green', linestyle='dashed', linewidth=2)

        plt.axvline(Yangon_sales.mean()+t_stat[0]*Yangon_sales.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
        plt.axvline(Mandalay_sales.mean()-t_stat[0]*Mandalay_sales.std(), color='black', linestyle='dashed', linewidth=2)

        plt.legend()
        plt.show()
        st.pyplot(fig)


    with st.expander('Show Conclusion'):
         st.markdown('''
         <h3>
        ✔️Accept Null Hypothesis✔️
         </h3>
         ''', unsafe_allow_html=True)

         st.markdown('''
        The alt hypothesist blackline (H1) is within confidence interval. \
        this mean we fail to reject (H0), because there has similar income between two cities.
        
        ''')

    with st.expander('Analysist'):
         st.markdown('''
        For sales development, the city of Naypyitaw has the highest income \
        because the product that has the highest gross income is \
        Food & Beverages whose sales are in the city of Naypyitaw, \
        in other words other cities such as Yangon & Mandalay \
        also have products with the highest sales respectively, \
        so as to maximize product quantity. of each city should be maximized. \
        From this we can try to maximize sales in the promotion of other \
        types of products that have high prices to get bigger profits.
        ''')
  
         
        
    
