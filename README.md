# 🏢 Commercial Escrow Operations Suite
### *Proof-of-Concept (PoC) Digital Workspace for Real Estate Transactions*

Welcome to the **Commercial Escrow Operations Suite**—a custom desktop dashboard engine built using Python and Streamlit. This application is designed specifically to optimize efficiency, lower transactional compliance risk, and eliminate manual bottlenecks in high-liability commercial real estate closings.

---

## 👔 Management Executive Brief (Value Abstract)
For decision-makers and commercial escrow managers, a high-volume commercial transaction pipelines represent significant legal and financial liability. A single missed wire cutoff, unverified entity signer, or miscalculated per-diem tax proration can cause multi-million dollar deals to fall through or result in post-closing escrow claims.

This operational suite solves those vulnerabilities by automating repetitive file-auditing and time-sensitive calculations:

*   **Risk Mitigation:** Scans incoming documents for critical title insurance markers and flags missing materials before closing day.
*   **Default Protection:** Provides real-time countdown alerts for local and regional bank wire deadlines to ensure same-day funding settlement.
*   **Operational Velocity:** Replaces spreadsheet formulas with an instant, interactive ledger that dynamically shifts settlement metrics as closing parameters evolve.

---

## 🧳 Operational Modules & User Guide

Navigate between these specialized tools using the clean sidebar layout on the left side of the screen.

### 🏢 1. The Welcome Workspace (Main)
*   **Purpose:** Serving as the central dashboard hub, this screen guides operators into their active transaction workflows. 
*   **How to Use:** Review the core tool functions listed on the central panel and click any utility in the left navigation sidebar to launch a task workspace.

### 🔍 2. 'Clean Title' Document Tracker
*   **Purpose:** Eliminates manual text-skimming by running automated phrase matching against incoming PDF files to verify closing readiness.
*   **How to Use:**
    1. Drag and drop single or multiple closing documents into the **Document Upload Center** on the left sidebar.
    2. The engine instantly extracts raw text structures and checks them against the **Title Compliance Checklist** (e.g., verifying *Payoff Statements*, *Lien Releases*, *Entity Corporate Resolutions*, and *Title Insurance Commitments*).
    3. View the live **File Completion Rate** progress bar.
    4. Review **Smart Risk Alerts**—such as system warnings to verify "Good Through" dates on detected payoffs—to address issues before files proceed to funding.

### 🧮 3. Commercial Closing Statement Calculator
*   **Purpose:** A digital sandtable to model calculations, test ALTA/HUD statement inputs, and distribute closing line-items dynamically.
*   **How to Use:**
    1. Enter transaction figures under **Transaction Details** (Purchase Price, Earnest Deposits, Loan Amounts, and Property Taxes).
    2. Enter fees under **Title, Escrow & Recording Fees** and use the interactive dropdown selectors to allocate costs (*Split 50/50*, *Buyer Pays Entirely*, *Seller Pays Entirely*).
    3. Input custom entries (such as broker commissions or survey fees) under the **Dynamic Miscellaneous Adjustments** panel.
    4. Click **🔄 Run Balancing Math** to view a perfectly formatted, double-entry **Trial Balance Ledger** tracking specific net wire requirements for buyers and sellers.

### ⏰ 4. Critical Date & Wire Deadline Alerts
*   **Purpose:** Prevents title defaults and funding delays by tracking contract milestones alongside real-time commercial banking deadlines.
*   **How to Use:**
    1. Use the **Wire Deadline Settings** panel on the left sidebar to select your active regional time zone and target banking entity cutoff time.
    2. The system calculates a real-time countdown banner: **Green** for stable windows, **Yellow** for approaching limits, and **Red** for critical wire crunches or closed banking hours.
    3. Use the **Active Transaction Milestone Audit** form to input contract dates and window durations. The calculation engine will map exact calendar deadlines for title objections, financing contingencies, and closing days.

### 📋 5. Entity Verification & KYC Assistant
*   **Purpose:** Organizes and verifies signature paths for complex signing structures (such as multi-tier LLCs, corporate managing members, and trusts).
*   **How to Use:**
    1. Fill out the **Add Signing Authority Record** form with the entity name, authorized individual signer, and exact title capacity.
    2. Check off the specific organizational documents reviewed during your compliance check.
    3. Click **➕ Log Signer Authority** to save the record down into an interactive, digital **Transaction Signing Authority Registry** log.
    4. Use the built-in **Underwriting Verification Reminders** at the bottom of the page to maintain full regulatory compliance for LLC and corporate files.

---

## 💻 Technical Infrastructure & Local Installation

This application runs locally or via your preferred cloud hosting provider, requiring minimal resource overhead.

### Prerequisites
Ensure you have **Python 3.9+** installed on your system.

### Installation Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com
   cd Commercial-Escrow-Agent-Suite
   ```

2. **Install Required Package Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Local Core Server:**
   ```bash
   streamlit run Main.py
   ```
   *The application will boot up immediately and display inside a new window in your default web browser.*

---

## 🛠️ Technology Stack
*   **UI Framework:** [Streamlit](https://streamlit.io) (Data-focused reactive dashboard architecture)
*   **PDF Extraction Processing Engine:** [pdfplumber](https://github.com) (High-accuracy character and positional text parsing)
*   **Timezone & Clock Management:** [pytz](https://pythonhosted.org) (Precise Olson-database timezone mapping)
*   **Data Structures:** [Pandas](https://pydata.org) (In-memory structured data tables)

---

## 📺 Screenshots
<img width="1000" height="385" alt="image" src="https://github.com/user-attachments/assets/6895f16b-7a5d-4a11-803a-84d424b70f06" />
<br>
<img width="1000" height="477" alt="image" src="https://github.com/user-attachments/assets/5e43e456-c035-442c-b205-3cca94c15122" />
<br>
<img width="1000" height="444" alt="image" src="https://github.com/user-attachments/assets/bdd5e419-82b0-492f-8e1e-4dcc62bb6bc8" />
<br>
<img width="1000" height="438" alt="image" src="https://github.com/user-attachments/assets/3fa17e4e-d2cb-4507-9897-e8927e302bde" />
<br>
<img width="1000" height="448" alt="image" src="https://github.com/user-attachments/assets/d7dd8bdc-c45a-431d-b2e0-309e4df9a57e" />

*Disclaimer: This software is provided as an operational Proof of Concept (PoC) tool designed to assist escrow professionals with pipeline data analysis. It should be used alongside primary internal title underwriting platforms.*
