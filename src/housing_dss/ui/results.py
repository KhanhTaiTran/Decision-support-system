"""Result tables and explanations for the TOPSIS recommendation view."""

from typing import Any

import streamlit as st

from housing_dss.criteria import CRITERIA


def format_rooms(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Map ranking records to the English column labels shown in the app."""
    labels = {key: value[0] for key, value in CRITERIA.items()}
    return [
        {
            "ID": room["id"],
            "Room": room["name"],
            **{labels[key]: room[key] for key in CRITERIA},
            "TOPSIS score": round(room["score"], 4),
        }
        for room in rows
    ]


def render_ranked_rooms(ranked: list[dict[str, Any]], weights: dict[str, int]) -> None:
    """Render the ranked rooms, including complete results and calculation data."""
    if not ranked:
        st.info("No rooms match your budget. Increase the budget to explore more options.")
        return
    if len(ranked) == 1:
        st.info("Only one room meets your budget. There are no other eligible options to compare.")

    st.subheader(f"Top {min(3, len(ranked))} of {len(ranked)} eligible rooms")
    st.dataframe(format_rooms(ranked[:3]), width="stretch", hide_index=True)
    st.caption(
        "Scores indicate relative preference within the current candidate set, not a probability "
        "of suitability. Tied rooms are displayed by ID. Indistinguishable alternatives receive "
        "a score of 0.5."
    )

    with st.expander("All results"):
        st.dataframe(format_rooms(ranked), width="stretch", hide_index=True)

    with st.expander("Calculation method and current weights"):
        labels = {key: value[0] for key, value in CRITERIA.items()}
        total = sum(weights.values())
        st.write({labels[key]: f"{value / total:.1%}" for key, value in weights.items()})
        st.write(
            "Filter by budget -> normalize vectors -> apply weights -> identify ideal solutions "
            "using cost/benefit directions -> calculate D+, D- -> C = D- / (D+ + D-)."
        )
        st.dataframe(
            [
                {"ID": room["id"], "D+": room["d_plus"], "D-": room["d_minus"], "C": room["score"]}
                for room in ranked
            ],
            hide_index=True,
        )
