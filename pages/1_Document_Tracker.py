import streamlit as st
import pdfplumber

# CRITICAL FIX: Removed st.set_page_config because it is already handled in main.py

st.title("🔍 'Clean Title' Document Tracker")
st.subheader("Automated Closing Document Audit & Keyword Scan")
st.markdown("---")

# Define the Escrow Checklist and target keywords to search for
REQUIRED_DOCUMENTS = {
    "Payoff Statement": ["payoff", "good through", "per diem", "wire instructions"],
    "Lien Release / Satisfaction": ["release of lien", "satisfaction of mortgage", "discharge"],
    "Entity Authorization (LLC/Corp)": ["operating agreement", "resolution", "authorized signatory", "incumbency"],
    "Title Insurance Commitment": ["schedule a", "schedule b", "requirements", "exceptions"]
}

# Sidebar Configuration for Uploads
st.sidebar.header("📁 Document Upload Center")
uploaded_files = st.sidebar.file_uploader(
    "Drag and drop closing PDFs here", 
    type=["pdf"], 
    accept_multiple_files=True
)

# Main App Logic
if not uploaded_files:
    st.info("💡 **How to use:** Upload one or more transaction PDFs in the sidebar to run an automated escrow compliance audit.")
else:
    st.success(f"Successfully loaded {len(uploaded_files)} document(s). Processing text extraction...")
    
    # Extract text from all uploaded files combined
    all_extracted_text = ""
    with st.spinner("Analyzing PDF text structures..."):
        for uploaded_file in uploaded_files:
            try:
                with pdfplumber.open(uploaded_file) as pdf:
                    for page in pdf.pages:
                        text = page.extract_text()
                        if text:
                            all_extracted_text += text.lower() + "\n"
            except Exception as e:
                st.error(f"Error reading {uploaded_file.name}: {e}")

    # UI Columns for Results Display
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📋 Title Compliance Checklist")
        st.write("System audit based on automated phrase matching:")
        
        # Track found status to display summary later
        found_statuses = {}

        for doc_name, keywords in REQUIRED_DOCUMENTS.items():
            # Check if any of the keywords appear in the extracted text
            is_found = any(keyword in all_extracted_text for keyword in keywords)
            found_statuses[doc_name] = is_found
            
            # Render visual indicator icons
            if is_found:
                st.markdown(f"### ✅ {doc_name}")
                st.caption("Matches found in the uploaded text pool.")
            else:
                st.markdown(f"### ❌ {doc_name} (Missing or Unverified)")
                st.caption(f"Could not verify. Looking for terms like: {', '.join(keywords)}")
            st.markdown("---")

    with col2:
        st.subheader("📊 Audit Summary & Flagged Risks")
        
        # Calculate completion metrics
        total_docs = len(REQUIRED_DOCUMENTS)
        docs_found = sum(1 for status in found_statuses.values() if status)
        completion_rate = docs_found / total_docs
        
        st.metric(label="File Completion Rate", value=f"{int(completion_rate * 100)}%")
        st.progress(completion_rate)
        
        # Proactive Escrow Warnings
        st.markdown("### ⚠️ Smart Risk Alerts")
        alerts_triggered = 0
        
        if found_statuses["Payoff Statement"]:
            st.warning("**Payoff Expiration Risk:** A payoff statement was detected. Ensure the 'Good Through' date covers the projected wire date.")
            alerts_triggered += 1
            
        if not found_statuses["Entity Authorization (LLC/Corp)"]:
            st.error("**Signatory Risk:** No clear entity authorization text found. Double-check corporate resolutions for signing authority.")
            alerts_triggered += 1
            
        if alerts_triggered == 0:
            st.success("No immediate operational flags triggered for the scanned documents.")
