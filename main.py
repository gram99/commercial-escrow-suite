import streamlit as st

# 1. Page Configuration (Must be handled at the entry point router)
st.set_page_config(
    page_title="Kensington Vanguard Escrow Suite",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Centralized Master Multi-Page Navigation Structure
pg = st.navigation({
    "Escrow Hub": [
        st.Page("pages/0_Main.py", title="Main", icon="🏢"),
    ],
    "Operational Tools": [
        st.Page("pages/1_Document_Tracker.py", title="Document Tracker", icon="🔍"),
        st.Page("pages/2_Closing_Calc.py", title="Closing Calc", icon="🮮"),
        st.Page("pages/3_Deadline_Alerts.py", title="Deadline Alerts", icon="⏰"),
        st.Page("pages/4_Entity_Verifier.py", title="Entity Verifier", icon="📋"),
    ]
})
