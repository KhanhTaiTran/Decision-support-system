"""Run after installation: python -m streamlit run app.py."""

from pathlib import Path
import streamlit as st
from housing_dss.data import load_rooms
from housing_dss.topsis import rank_rooms
from housing_dss.ui.preferences import render_preferences
from housing_dss.ui.results import render_ranked_rooms

st.set_page_config(page_title="Student Housing DSS", layout="wide")
st.title("Student Housing Decision Support")
st.caption("Starter version. Synthetic data for development and demonstrations, not actual rental listings.")

budget, weights = render_preferences()

try:
    rooms = load_rooms(Path(__file__).parent / "data" / "rooms_sample.csv")
    eligible = [room for room in rooms if room["monthly_cost_vnd"] <= budget]
    ranked = rank_rooms(eligible, weights)
except (ValueError, OSError) as error:
    st.error(str(error))
    st.stop()

render_ranked_rooms(ranked, weights)
