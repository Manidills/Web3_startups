from explore import explore
from fundings import fundings
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt
from streamlit_option_menu import option_menu


# Layout
st.set_page_config(page_title="Web3_AI",
    page_icon="chart_with_upwards_trend",layout="wide")

padding_top = 0

st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            padding-top: {padding_top}rem;
        }}
    </style>""",
    unsafe_allow_html=True,
)

IMAGE = "https://media.tenor.com/Rooi8rhW1CkAAAAi/web3-crypto.gif"

a, b= st.columns([1,2])
a.image(IMAGE, width=200)
b.title("WEB3 AI STARTUPS FUNDINGS")
st.markdown("##")
st.markdown("##")




option =  option_menu("WEB3_AI", ["About", "Fundings", "Explore"],
                         icons=['house', 'camera fill', 'kanban'],
                         menu_icon="app-indicator", default_index=0,orientation="horizontal",
                         styles={
        "container": {"padding": "5!important", "background-color": "black"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "black"},
    }
    )

if option == 'About':
   st.write("Web3 AI startups are companies that leverage the latest advancements in artificial intelligence (AI) and blockchain technology to create innovative solutions for the decentralized web. These startups are at the forefront of a new era of computing, where data is owned and controlled by individuals, and applications can be built on top of decentralized networks that are not controlled by any single entity.")
   st.markdown("##")
   st.write("""

   Here a list of top web3 AI startups and there funding datas including SERIES B  

   ### Anchain-ai: Provides blockchain intelligence and analysis for the cryptocurrency industry.

   ### Bitquery: Offers blockchain data APIs and a blockchain explorer.

   ### Bitscrunch: A blockchain analytics company that focuses on supply chain transparency and sustainability.

   ### Blur-exchange: A decentralized finance (DeFi) protocol for privacy-preserving transactions with AI.

   ### Chainalysis: A blockchain data analytics company that provides cryptocurrency investigation and compliance solutions.

   ### Coinbase AI: A leading cryptocurrency exchange and digital asset platform.

   ### Connext-inc: A layer 2 scaling solution for Ethereum.

   ### Consensus Systems: A blockchain research and development firm.

   ### Covalent: Offers a unified API for full transparency into blockchain data

   ### Deepnftvalue: Uses machine learning to evaluate the value of non-fungible tokens (NFTs).

   ### Dune-analytics: A community-driven platform for data analytics on the Ethereum blockchain.

   ### Ethereum-push-notification-service: A decentralized notification service for Ethereum smart contracts.

   ### Fetch-ai: A decentralized machine learning platform.

   ### Filecoin: A decentralized storage network.

   ### Guardian-link: A decentralized identity and access management solution.

   ### Immunefi: A bug bounty platform for smart contracts and DeFi projects.

   ### Livepeer: A decentralized video streaming platform.

   ### Ml-tech: A blockchain-based machine learning marketplace.

   ### Moralis: A Web3 backend infrastructure provider.

   ### Nftgo: A social network for NFT collectors and creators.

   ### Nftically: A marketplace for NFTs.

   ### Nftport: A platform for transferring NFTs between different blockchains.

   ### Numerai: A blockchain-based hedge fund that uses machine learning to trade on financial markets.

   ### Pinata-59fc: A decentralized file storage and content delivery network (CDN) for Web3.

   ### Quiknode: A platform for running Ethereum nodes.

   ### Shardeum: A blockchain-based platform for secure data sharing and collaboration.

   ### SingularityNET: A decentralized AI marketplace.

   ### Upshot-d781: A decentralized prediction market platform.
   
   """)

elif option == 'Fundings':
    fundings()
elif option == 'Explore':
    explore()


st.info(f"Data source {'https://www.crunchbase.com/'}")

st.success("https://github.com/Manidills/Web3_startups")