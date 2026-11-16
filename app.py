"""Run after installation: python -m streamlit run app.py."""

from pathlib import Path
import streamlit as st
from housing_dss.criteria import CRITERIA
from housing_dss.data import load_rooms
from housing_dss.topsis import rank_rooms

st.set_page_config(page_title="Student Housing DSS", layout="wide")
st.title("Student Housing Decision Support")
st.caption("Starter version. Synthetic data for development and demonstrations, not actual rental listings.")

with st.sidebar:
    st.header("Your preferences")
    budget = st.number_input("Maximum monthly budget (VND)", min_value=0, value=4000000, step=100000)
    st.subheader("Criterion priorities")
    weights = {key: st.slider(label, 0, 100, 20, key=key) for key, (label, _) in CRITERIA.items()}

try:
    rooms = load_rooms(Path(__file__).parent / "data" / "rooms_sample.csv")
    eligible = [room for room in rooms if room["monthly_cost_vnd"] <= budget]
    ranked = rank_rooms(eligible, weights)
except (ValueError, OSError) as error:
    st.error(str(error))
    st.stop()

if not ranked:
    st.info("No rooms match your budget. Increase the budget to explore more options.")
    st.stop()
if len(ranked) == 1:
    st.info("Only one room meets your budget. There are no other eligible options to compare.")

st.subheader(f"Top {min(3, len(ranked))} of {len(ranked)} eligible rooms")
labels = {key: value[0] for key, value in CRITERIA.items()}
def display(rows):
    return [{"ID": room["id"], "Room": room["name"],
             **{labels[key]: room[key] for key in CRITERIA},
             "TOPSIS score": round(room["score"], 4)} for room in rows]

st.dataframe(display(ranked[:3]), width="stretch", hide_index=True)
st.caption("Scores indicate relative preference within the current candidate set, not a probability of suitability. "
           "Tied rooms are displayed by ID. Indistinguishable alternatives receive a score of 0.5.")
with st.expander("All results"):
    st.dataframe(display(ranked), width="stretch", hide_index=True)
with st.expander("Calculation method and current weights"):
    total = sum(weights.values())
    st.write({labels[key]: f"{value / total:.1%}" for key, value in weights.items()})
    st.write("Filter by budget → normalize vectors → apply weights → identify ideal solutions "
             "using cost/benefit directions → calculate D+, D- → C = D- / (D+ + D-).")
    st.dataframe([{"ID": r["id"], "D+": r["d_plus"], "D-": r["d_minus"], "C": r["score"]}
                  for r in ranked], hide_index=True)
