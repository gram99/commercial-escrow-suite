import streamlit as st

# 1. Page Configuration (Must be the first command on this sub-page)
st.set_page_config(
    page_title="Kensington Vanguard Escrow Suite",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Force a Custom Clean Navigation Menu (Hides the root main.py file)
st.sidebar.page_link("pages/0_Main.py", label="Main", icon="🏢")
st.sidebar.page_link("pages/1_Document_Tracker.py", label="Document Tracker", icon="🔍")
st.sidebar.page_link("pages/2_Closing_Calc.py", label="Closing Calc", icon="🧮")
st.sidebar.page_link("pages/3_Deadline_Alerts.py", label="Deadline Alerts", icon="⏰")
st.sidebar.page_link("pages/4_Entity_Verifier.py", label="Entity Verifier", icon="📋")

st.sidebar.markdown("---")

# 3. Main Welcome Dashboard UI Content
st.title("🏢 Commercial Escrow Operations Suite")
st.subheader("Proof of Concept Workflow Productivity Tools")
st.markdown("---")

st.markdown("""
### Welcome to your Digital Escrow Assistant
Select a tool from the sidebar navigation to streamline your daily commercial closing pipeline:

*   **🔍 Document Tracker:** Scan PDF files to automatically verify required title documents and look for expiration dates.
*   **🧮 Closing Calculator:** Simulate closing dates, calculate interest prorations, and audit debit/credit balances.
*   **⏰ Deadline Alerts:** View a daily countdown of wire cutoff times and critical contract milestones.
*   **📋 Entity Verifier:** Map out complex corporate signing structures and cross-reference authorization documents.
""")

st.info("💡 **Tip:** Use the sidebar menu on the left to seamlessly jump between different active transaction tasks.")
