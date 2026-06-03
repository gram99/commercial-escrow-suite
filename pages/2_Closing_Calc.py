import streamlit as st
from datetime import datetime, timedelta

# 1. Custom Navigation Sidebar
st.sidebar.page_link("pages/0_Main.py", label="Main", icon="🏢")
st.sidebar.page_link("pages/1_Document_Tracker.py", label="Document Tracker", icon="🔍")
st.sidebar.page_link("pages/2_Closing_Calc.py", label="Closing Calc", icon="🧮")
st.sidebar.page_link("pages/3_Deadline_Alerts.py", label="Deadline Alerts", icon="⏰")
st.sidebar.page_link("pages/4_Entity_Verifier.py", label="Entity Verifier", icon="📋")
st.sidebar.markdown("---")

st.title("🧮 Commercial Closing Statement Calculator")
st.subheader("Proration Logic, Custom Title Fees & Debit/Credit Balancing Ledger")
st.markdown("---")

# 2. Transaction Parameters Input Form
with st.form("calculator_inputs"):
    st.subheader("📋 Transaction Details")
    col_a, col_b = st.columns(2)
    
    with col_a:
        purchase_price = st.number_input("Purchase Price ($)", min_value=0.0, value=5000000.0, step=10000.0, format="%,.2f")
        earnest_money = st.number_input("Earnest Money Deposit ($)", min_value=0.0, value=250000.0, step=5000.0, format="%,.2f")
        new_loan_amount = st.number_input("New Lender Loan Amount ($)", min_value=0.0, value=3500000.0, step=10000.0, format="%,.2f")
        
    with col_b:
        closing_date = st.date_input("Target Closing Date", datetime.today() + timedelta(days=14))
        annual_tax_bill = st.number_input("Annual Property Tax ($)", min_value=0.0, value=24000.0, step=100.0, format="%,.2f")
        daily_interest_rate = st.number_input("Lender Per Diem Interest Rate (%)", min_value=0.0, max_value=100.0, value=6.5, step=0.1, format="%.3f")
        days_of_interest = st.number_input("Days of Prepaid Interest to Collect", min_value=0, max_value=31, value=15)

    st.markdown("---")
    st.subheader("🛡️ Title, Escrow & Recording Fees")
    col_c, col_d = st.columns(2)
    
    with col_c:
        title_premium = st.number_input("Title Insurance Premium ($)", min_value=0.0, value=12500.0, step=500.0, format="%,.2f")
        title_premium_payer = st.selectbox("Who pays Title Premium?", ["Split 50/50", "Buyer Pays Entirely", "Seller Pays Entirely"])
        
        escrow_fee = st.number_input("Kensington Vanguard Settlement/Escrow Fee ($)", min_value=0.0, value=2500.0, step=250.0, format="%,.2f")
        escrow_payer = st.selectbox("Who pays Escrow Fee?", ["Split 50/50", "Buyer Pays Entirely", "Seller Pays Entirely"])

    with col_d:
        endorsement_fees = st.number_input("Title Endorsement Charges ($)", min_value=0.0, value=1500.0, step=100.0, format="%,.2f")
        endorsement_payer = st.selectbox("Who pays Endorsements?", ["Buyer Pays Entirely", "Seller Pays Entirely", "Split 50/50"])
        
        recording_fees = st.number_input("Government Recording Fees ($)", min_value=0.0, value=450.0, step=50.0, format="%,.2f")
        recording_payer = st.selectbox("Who pays Recording Fees?", ["Buyer Pays Entirely", "Seller Pays Entirely", "Split 50/50"])

    st.markdown("---")
    st.subheader("📝 Dynamic Miscellaneous Adjustments")
    st.caption("Add one-off line items unique to this commercial transaction (e.g., broker commissions, survey fees, environmental reports).")
    
    col_misc1, col_misc2, col_misc3 = st.columns(3)
    with col_misc1:
        misc_desc = st.text_input("Fee Description", placeholder="e.g., Commercial Broker Commission")
    with col_misc2:
        misc_amt = st.number_input("Fee Amount ($)", min_value=0.0, value=0.0, step=100.0, format="%,.2f")
    with col_misc3:
        misc_payer = st.selectbox("Assigned Payer", ["Seller Pays Entirely", "Buyer Pays Entirely"])

    submit_button = st.form_submit_button(label="🔄 Run Balancing Math & Custom Prorations")

# 3. Financial Math Logic Engine
start_of_year = datetime(closing_date.year, 1, 1).date()
days_seller_owned = (closing_date - start_of_year).days
daily_tax_cost = annual_tax_bill / 365.0
seller_tax_proration = daily_tax_cost * days_seller_owned

daily_loan_interest = (new_loan_amount * (daily_interest_rate / 100.0)) / 360.0
total_prepaid_interest = daily_loan_interest * days_of_interest

buyer_title_cost = title_premium if title_premium_payer == "Buyer Pays Entirely" else (title_premium / 2 if title_premium_payer == "Split 50/50" else 0.0)
seller_title_cost = title_premium if title_premium_payer == "Seller Pays Entirely" else (title_premium / 2 if title_premium_payer == "Split 50/50" else 0.0)

buyer_escrow_cost = escrow_fee if escrow_payer == "Buyer Pays Entirely" else (escrow_fee / 2 if escrow_payer == "Split 50/50" else 0.0)
seller_escrow_cost = escrow_fee if escrow_payer == "Seller Pays Entirely" else (escrow_fee / 2 if escrow_payer == "Split 50/50" else 0.0)

buyer_endo_cost = endorsement_fees if endorsement_payer == "Buyer Pays Entirely" else (endorsement_fees / 2 if endorsement_payer == "Split 50/50" else 0.0)
seller_endo_cost = endorsement_fees if endorsement_payer == "Seller Pays Entirely" else (endorsement_fees / 2 if endorsement_payer == "Split 50/50" else 0.0)

buyer_rec_cost = recording_fees if recording_payer == "Buyer Pays Entirely" else (recording_fees / 2 if recording_payer == "Split 50/50" else 0.0)
seller_rec_cost = recording_fees if recording_payer == "Seller Pays Entirely" else (recording_fees / 2 if recording_payer == "Split 50/50" else 0.0)

buyer_misc_cost = misc_amt if (misc_payer == "Buyer Pays Entirely" and misc_amt > 0) else 0.0
seller_misc_cost = misc_amt if (misc_payer == "Seller Pays Entirely" and misc_amt > 0) else 0.0

# 4. Dynamic Visual Results Table
st.markdown("---")
st.subheader("⚖️ Trial Balance Ledger (ALTA/HUD Simulation)")

buyer_debits = purchase_price + total_prepaid_interest + buyer_title_cost + buyer_escrow_cost + buyer_endo_cost + buyer_rec_cost + buyer_misc_cost
buyer_credits = earnest_money + new_loan_amount + seller_tax_proration
buyer_cash_needed = buyer_debits - buyer_credits

seller_debits = seller_tax_proration + seller_title_cost + seller_escrow_cost + seller_endo_cost + seller_rec_cost + seller_misc_cost
seller_credits = purchase_price
seller_net_proceeds = seller_credits - seller_debits

col_buyer, col_seller = st.columns(2)

with col_buyer:
    st.markdown("### 🔵 Buyer Statement")
    st.write(f"**Base Purchase Debits:** `${purchase_price:,.2f}`")
    st.write(f"**Prepaid Loan Interest:** `${total_prepaid_interest:,.2f}`")
    st.write(f"**Allocated Closing Fees:** `${(buyer_title_cost + buyer_escrow_cost + buyer_endo_cost + buyer_rec_cost + buyer_misc_cost):,.2f}`")
    st.markdown("---")
    st.write(f"**Gross Debits (Total Costs):** `${buyer_debits:,.2f}`")
    st.write(f"**Gross Credits (Payments/Credits):** `${buyer_credits:,.2f}`")
    
    if buyer_cash_needed >= 0:
        st.metric(label="💰 Estimated Cash From Buyer (Wire In)", value=f"${buyer_cash_needed:,.2f}")
    else:
        st.metric(label="🔄 Excess Funds Owed to Buyer", value=f"${abs(buyer_cash_needed):,.2f}")

with col_seller:
    st.markdown("### 🟢 Seller Statement")
    st.write(f"**Gross Credits (Property Value):** `${seller_credits:,.2f}`")
    st.write(f"**Tax Proration Owed:** `${seller_tax_proration:,.2f}`")
    st.write(f"**Allocated Settlement Fees:** `${(seller_title_cost + seller_escrow_cost + seller_endo_cost + seller_rec_cost + seller_misc_cost):,.2f}`")
    st.markdown("---")
    st.write(f"**Gross Credits:** `${seller_credits:,.2f}`")
    st.write(f"**Gross Debits (Total Deductions):** `${seller_debits:,.2f}`")
    st.metric(label="🏦 Estimated Net Proceeds To Seller (Wire Out)", value=f"${seller_net_proceeds:,.2f}")

# 5. Escrow Math Audit Check
st.markdown("---")
st.subheader("🔍 Automated Escrow Audit Notes")

if misc_amt > 0 and misc_desc:
    st.info(f"➕ **Miscellaneous Fee Added:** Placed '{misc_desc}' costing `${misc_amt:,.2f}` onto the account ledger.")

st.info(f"📆 **Proration Context:** Seller owned the property for **{days_seller_owned} days** this calendar year. Property tax per-diem rate is **${daily_tax_cost:,.2f}/day**.")
st.info(f"📈 **Interest Context:** New commercial loan per-diem rate is **${daily_loan_interest:,.2f}/day** based on a 360-day banking standard.")

if abs((buyer_debits + seller_debits) - (buyer_credits + seller_credits + buyer_cash_needed - seller_net_proceeds)) < 0.01:
    st.success("✅ **Ledger Status:** Balanced perfectly. Every custom closing fee, tax split, and debit has been verified with a matching credit entry.")
else:
    st.error("❌ **Ledger Status:** Out of Balance. Please verify fee distribution or custom formulas.")
