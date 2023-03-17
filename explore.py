import math
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt
from streamlit_option_menu import option_menu
import numpy as np



def explore():
    data = pd.read_csv('web3_startup_funding.csv')
    data = data[['name', 'round_name', 'no_of_investors_round','date','money_raised','lead_inverstor_name']]
    data['money_raised'] = data['money_raised'].str.replace(',', '').astype(float)
    data['no_of_investors_round'] = data['no_of_investors_round'].str.replace('—', '1').astype(float)
    data['date'] = data['date'].astype('datetime64[ns]')
    data['round_name'] = data['round_name'].str[:10]
    st.markdown("#")

    selected_name = st.radio('Select a name', data['name'].unique(), horizontal=True)

    df = data[data['name'] == selected_name]

    st.write("""   
        #### FUNDING ROUNDS DETAILS ####  """)
    st.markdown("#")
    st.dataframe(df)

    st.markdown("##")
    st.write("""
    ###  Money Raised Over Years  ###
    """)
    st.markdown("##")
    st.altair_chart(
        alt.Chart(df).mark_bar(color='white').encode(
            x='date:T',
            y="money_raised:Q",
            
        ).properties(
            width=800,
            height=300
        ),  use_container_width=True
    
                    )

    st.markdown("##")
    st.write("""
    ###  Money Raised Based on Series  ###
    """)
    st.markdown("##")
    st.altair_chart(
        alt.Chart(df).mark_bar(color='white').encode(
            x='round_name',
            y="money_raised:Q",
            
        ).properties(
            width=800,
            height=300
        ),  use_container_width=True
    
                    )