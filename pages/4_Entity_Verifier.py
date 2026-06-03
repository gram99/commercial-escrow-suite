import streamlit as st
import pandas as pd

st.title("📋 Entity Verification & KYC Assistant")
st.subheader("Corporate Signing Authority Mapping & Escrow KYC Log")
st.markdown("---")

# 1. Structure Explainer Box
st.info(
    "💡 **Escrow Protocol:** Use this module to map out multi-layer entity structures (e.g., a subsidiary LLC managed by a parent Corp) "
    "and log which resolutions, operating agreements, or incumbency certificates have been verified for closing day."
)

# Initialize Session State to track added signers dynamically in memory
if "signer_log" not in st.session_state:
    st.session_state.signer_log = []

# 2. Interactive Input Panel
st.subheader("🏢 Add Signing Authority Record")
with st.form("entity_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        entity_name = st.text_input("Name of Contracting Entity", placeholder="e.g., Acme Commercial Holdings, LLC")
        signing_individual = st.text_input("Authorized Individual Signer Name", placeholder="e.g., John Doe")
        title_position = st.text_input("Corporate Title / Capacity", placeholder="e.g., Managing Member / Vice President")
        
    with col2:
        parent_entity = st.text_input("Parent Entity / Managing Member (If Applicable)", placeholder="e.g., Acme Capital Corp (Parent)")
        docs_reviewed = st.multiselect(
            "Corporate Documents Reviewed & Verified",
            ["Operating Agreement", "Articles of Organization", "Corporate Resolution", "Incumbency Certificate", "Certificate of Good Standing", "ID/Passport Verified"]
        )
        auth_status = st.selectbox("Authority Verification Status", ["Verified - Fully Authorized", "Pending Legal Review", "Discrepancy / Missing Docs"])

    submit_signer = st.form_submit_button("➕ Log Signer Authority")

# Form Submission Logic
if submit_signer:
    if entity_name and signing_individual and title_position:
        new_record = {
            "Entity Name": entity_name,
            "Parent Entity": parent_entity if parent_entity else "N/A (Direct)",
            "Authorized Signer": signing_individual,
            "Title/Capacity": title_position,
            "Documents Verified": ", ".join(docs_reviewed) if docs_reviewed else "None",
            "Status": auth_status
        }
        st.session_state.signer_log.append(new_record)
        st.toast(f"Logged authority for {signing_individual}!", icon="✅")
    else:
        st.error("Please fill out the Entity Name, Signer Name, and Title fields to log the record.")

# 3. Dynamic Audit Ledger Display
st.markdown("---")
st.subheader("📑 Transaction Signing Authority Registry")

if st.session_state.signer_log:
    # Convert session state memory logs into a clean Pandas Dataframe for visual tables
    df = pd.DataFrame(st.session_state.signer_log)
    
    # Render interactive data table
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Clear logs button
    if st.button("🗑️ Clear Authority Log"):
        st.session_state.signer_log = []
        st.rerun()
else:
    st.caption("No signing structures logged yet. Use the form above to build the escrow authority map.")

# 4. Proactive Title Underwriting Checklist
st.markdown("---")
st.subheader("🛡️ Escrow Underwriting Verification Reminders")

col_chk1, col_chk2 = st.columns(2)

with col_chk1:
    st.markdown("##### 📌 LLC Verification Protocol")
    st.markdown("- [ ] Check Secretary of State portal to confirm entity is **Active & In Good Standing**.")
    st.markdown("- [ ] Cross-reference Operating Agreement Schedule A to verify members.")
    st.markdown("- [ ] If manager-managed, verify the specific manager is signing.")

with col_chk2:
    st.markdown("##### 📌 Corporation / Trust Protocol")
    st.markdown("- [ ] Confirm Corporate Resolution specifically names the real estate transaction.")
    st.markdown("- [ ] Verify the resolution is signed by the **Corporate Secretary**.")
    st.markdown("- [ ] For Trusts, review relevant sections of the full **Trust Agreement** or Certification.")
