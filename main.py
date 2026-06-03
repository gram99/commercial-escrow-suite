import streamlit as st

# Page Configuration (Must be handled at the very top)
st.set_page_config(
    page_title="Kensington Vanguard Escrow Suite",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main Welcome Dashboard UI Content
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
