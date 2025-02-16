import streamlit as st
from googleapiclient.discovery import build
import plotly.graph_objects as go

# Replace with your own function imports
from utils import get_channel_stats, get_video_stats, search_videos

st.set_page_config(layout="wide", page_title="YouTube Insights")

st.title("YouTube Insights Tool (vidIQ-style)")

# Securely store API key in Streamlit secrets
api_key = st.secrets["AIzaSyCID6TRLIk4krNLu5BpUkDXpTfhbQaZScs"]

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(["Channel Overview", "Video Analysis", "Keyword Research"])

# ---- CHANNEL OVERVIEW ----
with tab1:
    st.subheader("Channel Overview")
    channel_id = st.text_input("Enter a Channel ID:", value="UC_x5XG1OV2P6uZZ5FSM9Ttw")  # e.g., Google Developers
    if st.button("Get Channel Stats"):
        data = get_channel_stats(api_key, channel_id)
        if data:
            st.write(f"**Channel Title**: {data['title']}")
            st.write(f"**Subscribers**: {data['subscribers']}")
            st.write(f"**Total Views**: {data['views']}")
            st.write(f"**Video Count**: {data['videoCount']}")
        else:
            st.error("Channel not found or invalid Channel ID")

# ---- VIDEO ANALYSIS ----
with tab2:
    st.subheader("Video Analysis")
    video_id = st.text_input("Enter a Video ID:", value="dQw4w9WgXcQ")  # example
    if st.button("Get Video Stats"):
        stats = get_video_stats(api_key, video_id)
        if stats:
            st.write(f"**Title**: {stats['title']}")
            st.write(f"**Views**: {stats['views']}")
            st.write(f"**Likes**: {stats['likes']}")
            st.write(f"**Comments**: {stats['comments']}")
        else:
            st.error("Video not found or invalid Video ID")

# ---- KEYWORD RESEARCH ----
with tab3:
    st.subheader("Keyword / Search Analysis")
    query = st.text_input("Enter a search term:", value="AI tutorial")
    if st.button("Search"):
        results = search_videos(api_key, query)
        for item in results:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            channel_title = item["snippet"]["channelTitle"]
            st.write(f"**Video Title**: {title}")
            st.write(f"Channel: {channel_title}")
            st.write(f"Video ID: {video_id}")
            st.markdown("---")
