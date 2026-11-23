"""Sidebar widgets for collecting a student's housing preferences."""

import streamlit as st

from housing_dss.criteria import CRITERIA


def render_preferences() -> tuple[int, dict[str, int]]:
    """Render the sidebar and return the selected budget and criterion weights."""
    with st.sidebar:
        st.header("Your preferences")
        budget = st.number_input(
            "Maximum monthly budget (VND)",
            min_value=0,
            value=4000000,
            step=100000,
        )
        st.subheader("Criterion priorities")
        weights = {
            key: st.slider(label, 0, 100, 20, key=key)
            for key, (label, _) in CRITERIA.items()
        }

    return int(budget), weights
