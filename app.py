import streamlit as st
import pandas as pd

# Load Data
batters = pd.read_csv("IPL2025Batters.csv")

bowlers = pd.read_csv("IPL2025Bowlers.csv")

auction = pd.read_csv("auction.csv")

st.set_page_config(
    page_title="IPL AI Dashboard",
    layout="wide"
)

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "Team Analyzer",
        "Player Search",
        "Match Prediction",
        "Auction Analysis"
    ]
)

# HOME
if page == "Home":

    st.title("🏏 IPL AI Dashboard")

    orange = batters.sort_values("Runs", ascending=False).iloc[0]
    purple = bowlers.sort_values("WKT", ascending=False).iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Orange Cap", orange["Player Name"], orange["Runs"])

    with col2:
        st.metric("Purple Cap", purple["Player Name"], purple["WKT"])

# TEAM ANALYZER
elif page == "Team Analyzer":

    st.title("📊 Team Analyzer")

    team = st.selectbox(
        "Select Team",
        sorted(batters["Team"].unique())
    )

    runs = batters[batters["Team"] == team]["Runs"].sum()
    wkts = bowlers[bowlers["Team"] == team]["WKT"].sum()

    st.metric("Runs", runs)
    st.metric("Wickets", wkts)

# PLAYER SEARCH
elif page == "Player Search":

    st.title("🔥 Player Search")

    player = st.text_input("Enter Player Name")

    if player:

        batter = batters[
            batters["Player Name"].str.contains(player, case=False, na=False)
        ]

        bowler = bowlers[
            bowlers["Player Name"].str.contains(player, case=False, na=False)
        ]

        if not batter.empty:
            st.dataframe(batter)

        elif not bowler.empty:
            st.dataframe(bowler)

        else:
            st.error("Player Not Found")

# MATCH PREDICTION
elif page == "Match Prediction":

    st.title("🏏 Match Prediction")

    st.info("Prediction module coming next")

# AUCTION ANALYSIS
elif page == "Auction Analysis":

    st.title("💰 Auction Analysis")

    st.dataframe(
        auction.sort_values("PRICE PAID", ascending=False).head(10)
    )
