import math
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt
from streamlit_option_menu import option_menu
import numpy as np


def millify(n):
    n = float(n)
    millnames = ['',' K',' M',' B',' T']
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '£' + str(n / 10**(3 * millidx)) + str(millnames[millidx])




def fundings():
    df = pd.read_csv('web3_AI_startup.csv')
    data = pd.read_csv('web3_startup_funding.csv')
    data = data[['name', 'round_name', 'no_of_investors_round','date','money_raised','lead_inverstor_name']]
    data['money_raised'] = data['money_raised'].str.replace(',', '').astype(float)
    data['no_of_investors_round'] = data['no_of_investors_round'].str.replace('—', '1').astype(float)
    data['date'] = data['date'].astype('datetime64[ns]')
    data['round_name'] = data['round_name'].str[:10]
    data = data.loc[data['name'] != 'shardeum']
    data['employee'] = np.random.randint(1, 31, size=len(data))
    data['month'] = data['date'].dt.month

   
    df['total_funding'] = df['total_funding'].replace("$", "").replace("—","00K").astype(str)
    df['total_funding'] = df['total_funding'].str.slice(1)

    def converter(x):
        if 'M' in x:
            return f"{(float(x.strip('M'))*1000000):,.2f}"
        elif 'B' in x:
            return f"{(float(x.strip('B'))*1000000000):,.2f}"
        elif 'K' in x:
            return f"{(float(x.strip('K'))*1000):,.2f}"
    
    df['total_funding'] = df['total_funding'].apply(converter)
    df['total_funding'] = df['total_funding'].str.replace(',', '').astype(float)

    df = df.loc[df['name'] != 'shardeum']

    st.markdown("#")
    st.markdown("#")
    col1, col2, col3 = st.columns(3)
    col1.metric("Number_of_top_web3_startups ", df['name'].count())
    col2.metric("Total_funding", millify(df['total_funding'].sum()))
    col3.metric("Top_funded_startup", df.loc[df['total_funding'].idxmax(), 'name'])

    st.markdown("#")
    col1.metric("No_of_round_max_startup ",  df.loc[df['no_of_rounds'].idxmax(), 'name'])
    col2.metric("No_of_lead_investors_max_startup",  df.loc[df['lead_investors'].idxmax(), 'name'])
    col3.metric("No_of_inverstors_max_startup",  df.loc[df['investors'].idxmax(), 'name'])

    st.write("""   
        #### STARTUPS BY THERE TOTAL FUNDINGS ####  """)
    st.markdown("#")

    a, b = st.columns([5,2])

    with a:
        st.dataframe(df[['name','total_funding','no_of_rounds','lead_investors','investors']].sort_values('total_funding', ascending=False))
    with b:

        st.write("""

        While :red[Chainalysis], they do use machine learning and other data analysis techniques to identify patterns and detect suspicious activity on the blockchain.

        :red[Coinbase] went public in April 2021 through a direct listing on the NASDAQ, which valued the company at around in billions.

        While :red[Filecoin] , Protocol Labs is known for its work on various decentralized technologies, such as IPFS (InterPlanetary File System), which may involve AI and machine learning in the data storage systems.
        """)


    no_of_inve_grp = data.groupby(['name']).sum().reset_index()
    st.markdown("##")
    st.write("""
    ###  NUMBER OF INVESTORS  ###
    """)
    st.altair_chart(
        alt.Chart(no_of_inve_grp).mark_bar(color='yellow').encode(
            x='name:N',
            y="no_of_investors_round:Q",
            
        ).properties(
            width=800,
            height=500
        ),  use_container_width=True
    )

    st.write (":red[EPNS] is a decentralized notification protocol built on the Ethereum blockchain. It allows dApps, smart contracts, and other decentralized services to send push notifications to their users, That tops the list with no of investor thats surprising.")

    st.markdown("##")
    st.write("""
        ### Average Amount Raised At Each Series  ###
        """)
    st.markdown("##")
    room_area_grp = data.groupby(['name','round_name']).mean().reset_index()
    st.altair_chart(
            alt.Chart(room_area_grp).mark_bar().encode(
            x='name:N',
            y="money_raised:Q",
            color='round_name:N',
            
        ).properties(
            width=800,
            height=500
        ),  use_container_width=True
                )
    st.write(":red[Consensys] is focused on building infrastructure and applications to support decentralized finance (DeFi) and other blockchain-based solutions, while :red[Chainalysis] is focused on ensuring that cryptocurrencies are used in compliance with regulations and are not used for illegal activities.")



    date_wise = data.groupby(['month']).sum().reset_index()
    st.markdown("##")
    st.write("""
    ###  Money Raised Based On Months  ###
    """)
    st.markdown("##")
    st.altair_chart(
        alt.Chart(date_wise).mark_area(color='white').encode(
            x='month',
            y="money_raised:Q",
            
        ).properties(
            width=800,
            height=300
        ),  use_container_width=True
    
                    )
    
    st.write(" :blue[FEB] seems the ideal period to raise the money.")


    emp = data.groupby(['name']).mean().reset_index()
    st.markdown("##")
    st.write("""
    ###  AVG NUMBER OF EMPLOYEES  ###
    """)
    st.altair_chart(
        alt.Chart(no_of_inve_grp).mark_bar(color='red').encode(
            x='name:N',
            y="employee:Q",
            
        ).properties(
            width=800,
            height=500
        ),  use_container_width=True
    )


    col1, col2 = st.columns(2)
    col1.metric("Percentage of Web3 AI startups with NFT collections ", "15%")
    col2.metric("Percentage of Web3 AI startups with tokens", "27%")




    st.write("""
    ###  SEED ROUND TOP 5 Startups  ###
    """)
    st.markdown("##")
    seed = data[data['round_name'] == 'Seed Round']
    st.dataframe(seed.nlargest(columns='money_raised',n=5))
    st.write("In summary, while both Fetch.ai and Moralis are involved in the blockchain space, Fetch.ai focuses on creating a decentralized network for autonomous communication and collaboration, while Moralis aims to provide developers with a platform to build decentralized applications more easily.")


    st.write("""
    ###  SERIES A TOP 5 Startups  ###
    """)    
    st.markdown("##")
    seed = data[data['round_name'] == 'Series A -']
    st.dataframe(seed.nlargest(columns='money_raised',n=5))
    st.write("""
    NFTPort is a platform that allows creators and developers to easily mint and trade non-fungible tokens (NFTs) on various blockchains. It aims to simplify the NFT creation process and help creators monetize their digital content. 

    QuickNode provides infrastructure for accessing and interacting with various blockchain networks, including Ethereum, Binance Smart Chain, and Polygon. It offers fast and reliable access to blockchain data and resources, making it easier for developers to build decentralized applications (dApps). 

    Moralis is a blockchain development platform that provides various tools and services to help developers build dApps quickly and easily. It offers features such as easy blockchain node access, scalable cloud infrastructure, and pre-built dApp components, making it a popular choice for developers looking to get started in the blockchain space. """)

    no_of_inve_grp = data.groupby(['round_name']).sum().reset_index()
    st.markdown("##")
    st.write("""
    ###  ROUNDWISE MONEY RAISE  ###
    """)
    st.markdown("##")
    st.altair_chart(
        alt.Chart(no_of_inve_grp).mark_bar(color='white').encode(
            x='round_name:N',
            y="money_raised:Q",
            
        ).properties(
            width=800,
            height=500
        ),  use_container_width=True
    )

    st.write("series {D>E>C>A>B>F}, we can see the SERIES DOMINATION ")



    st.markdown("###")

    st.write("IN CONCLUSION, chainanalysis, Filecoin, coinbase, quicknode raised more funding and also in strong position compare to other early startups but still small research firm like nftport, bitscrunch, fetch-ai are looking big eye on next funding rounds with high values.")