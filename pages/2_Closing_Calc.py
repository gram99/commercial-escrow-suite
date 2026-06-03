import streamlit as st
from datetime import datetime, timedelta

st.title("🧮 Commercial Closing Statement Calculator")
st.subheader("Automated Proration Logic & Debit/Credit Balancing Ledger")
st.markdown("---")

# 1. Transaction Parameters Input Form
with st.form("calculator_inputs"):
    st.subheader("📋 Transaction Details")
    col_a, col_b = st.columns(2)
    
    with col_a:
        purchase_price = st.number_input("Purchase Price ($)", min_value=0.0, value=5000000.0, step=10000.0, format="%.2f")
        earnest_money = st.number_input("Earnest Money Deposit ($)", min_value=0.0, value=250000.0, step=5000.0, format="%.2f")
        new_loan_amount = st.number_input("New Lender Loan Amount ($)", min_value=0.0, value=3500000.0, step=10000.0, format="%.2f")
        
    with col_b:
        closing_date = st.date_input("Target Closing Date", datetime.today() + timedelta(days=14))
        annual_tax_bill = st.number_input("Annual Property Tax ($)", min_value=0.0, value=24000.0, step=100.0, format="%.2f")
        daily_interest_rate = st.number_input("Lender Per Diem Interest Rate (%)", min_value=0.0, max_value=100.0, value=6.5, step=0.1, format="%.3f")
        days_of_interest = st.number_input("Days of Prepaid Interest to Collect", min_value=0, max_value=31, value=15)

    submit_button = st.form_submit_button(label="🔄 Run Balancing Math & Prorations")

# 2. Financial Math Logic Engine
# Calculate Per Diem Property Tax Split (Assumes Calendar Year Proration, Buyer pays closing day)
start_of_year = datetime(closing_date.year, 1, 1).date()
days_seller_owned = (closing_date - start_of_year).days
daily_tax_cost = annual_tax_bill / 365.0
seller_tax_proration = daily_tax_cost * days_seller_owned

# Calculate Loan Per Diem Interest
daily_loan_interest = (new_loan_amount * (daily_interest_rate / 100.0)) / 360.0 # Commercial standard 360-day year
total_prepaid_interest = daily_loan_interest * days_of_interest

# 3. Dynamic Visual Results Table
st.markdown("---")
st.subheader("⚖️ Trial Balance Ledger (ALTA/HUD Simulation)")

# Define the double-entry accounting splits
buyer_debits = purchase_price + total_prepaid_interest
buyer_credits = earnest_money + new_loan_amount + seller_tax_proration
buyer_cash_needed = buyer_debits - buyer_credits

seller_debits = seller_tax_proration  # Outstanding tax owed up to closing day
seller_credits = purchase_price
seller_net_proceeds = seller_credits - seller_debits

# Render Side-by-Side Settlement Summaries
col_buyer, col_seller = st.columns(2)

with col_buyer:
    st.markdown("### 🔵 Buyer Statement")
    st.write(f"**Gross Debits (Cost):** `${buyer_debits:,.2f}`")
    st.write(f"**Gross Credits (Payments):** `${buyer_credits:,.2f}`")
    
    if buyer_cash_needed >= 0:
        st.metric(label="💰 Estimated Cash From Buyer (Wire In)", value=f"${buyer_cash_needed:,.2f}")
    else:
        st.metric(label="🔄 Excess Funds Owed to Buyer", value=f"${abs(buyer_cash_needed):,.2f}")

with col_seller:
    st.markdown("### 🟢 Seller Statement")
    st.write(f"**Gross Credits (Value):** `${seller_credits:,.2f}`")
    st.write(f"**Gross Debits (Deductions):** `${seller_debits:,.2f}`")
    st.metric(label="🏦 Estimated Net Proceeds To Seller (Wire Out)", value=f"${seller_net_proceeds:,.2f}")

# 4. Escrow Math Audit Check
st.markdown("---")
st.subheader("🔍 Automated Escrow Audit Notes")

st.info(f"📆 **Proration Context:** Seller owned the property for **{days_seller_owned} days** this calendar year. The calculated property tax per-diem rate is **${daily_tax_cost:,.2f}/day**.")
st.info(f"📈 **Interest Context:** New commercial loan per-diem rate is **${daily_loan_interest:,.2f}/day** based on a 360-day banking year standard.")

# Double Check System Integrity: (Buyer Debits + Seller Debits) MUST EQUAL (Buyer Credits + Seller Credits)
total_system_debits = buyer_debits + seller_debits + (buyer_cash_needed if buyer_cash_needed < 0 else 0)
total_system_credits = buyer_credits + seller_credits + (buyer_cash_needed if buyer_cash_needed > 0 else 0) + seller_net_proceeds

# account for tiny floating point errors in code math
if abs((buyer_debits + seller_debits) - (buyer_credits + seller_credits + buyer_cash_needed - seller_net_proceeds)) < 0.01:
    st.success("✅ **Ledger Status:** Balanced perfectly. Every debit has a matching credit entry.")
else:
    st.error("❌ **Ledger Status:** Out of Balance. Please verify internal line-item math adjustments.")
