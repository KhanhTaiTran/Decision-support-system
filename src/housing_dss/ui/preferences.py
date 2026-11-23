"""Sidebar widgets for collecting a student's housing preferences."""

import streamlit as st

from housing_dss.criteria import CRITERIA, DEFAULT_WEIGHT, PRESET_PROFILES


def _apply_preset(profile_name: str) -> None:
    """Callback to update session state sliders when a preset button is clicked."""
    if profile_name in PRESET_PROFILES:
        for criterion, weight in PRESET_PROFILES[profile_name].items():
            st.session_state[criterion] = weight


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
        st.caption("Preset Weight Profiles")

        for key in CRITERIA:
            if key not in st.session_state:
                st.session_state[key] = DEFAULT_WEIGHT

        col1, col2 = st.columns(2)
        with col1:
            st.button(
                "Balanced",
                key="preset_balanced",
                on_click=_apply_preset,
                args=("Balanced",),
                use_container_width=True,
                help="Equal priority across all criteria (20% each)",
            )
        with col2:
            st.button(
                "Budget-First",
                key="preset_budget_first",
                on_click=_apply_preset,
                args=("Budget-First",),
                use_container_width=True,
                help="Prioritize low monthly cost (60%)",
            )

        col3, col4 = st.columns(2)
        with col3:
            st.button(
                "Campus-Proximity",
                key="preset_campus_proximity",
                on_click=_apply_preset,
                args=("Campus-Proximity",),
                use_container_width=True,
                help="Prioritize proximity to campus (60%)",
            )
        with col4:
            st.button(
                "Comfort & Space",
                key="preset_comfort_space",
                on_click=_apply_preset,
                args=("Comfort & Space",),
                use_container_width=True,
                help="Prioritize floor area (35%), amenities (25%), and security (20%)",
            )

        weights = {
            key: st.slider(label, 0, 100, key=key)
            for key, (label, _) in CRITERIA.items()
        }

    return int(budget), weights

