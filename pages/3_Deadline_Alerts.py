import streamlit as st
from datetime import datetime, time

st.title("⏰ Critical Date & Wire Deadline Alerts")
st.subheader("Real-Time Escrow Milestones & Bank Funding Priority Queues")
st.markdown("---")

# 1. Wire Cutoff Priority Dashboard
st.subheader("🚨 Fedwire Cutoff Priority Queue")
st.write("Keep track of wire processing queues against standard commercial banking deadlines.")

# Define standard bank cutoffs (Can be adjusted)
WIRE_CUTOFF_HOUR = 16  # 4:00 PM
WIRE_CUTOFF_MIN = 30  # 30 minutes

now = datetime.now()
cutoff_time = datetime.combine(now.date(), time(WIRE_CUTOFF_HOUR, WIRE_CUTOFF_MIN))

# Calculate time remaining for wire processing today
if now < cutoff_time:
    time_remaining = cutoff_time - now
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    # Render countdown warning banner based on urgency
    if hours < 1:
        st.error(f"⚠️ **CRITICAL WIRE WARNING:** Only **{minutes} minutes** left before the standard 4:30 PM Fedwire deadline! Route immediate funding files now.")
    else:
        st.warning(f"⏳ **Wire Window Open:** **{hours} hours and {minutes} minutes** remaining to finalize disbursements for same-day bank settlement.")
else:
    st.error("🛑 **Fedwire Deadline Passed:** The standard 4:30 PM cutoff for same-day settlement has closed. Moving new wires will post next business day.")

st.markdown("---")

# 2. Pipeline Milestone Tracking Matrix
st.subheader("📂 Active Transaction Milestone Audit")
st.write("Input deal milestones to instantly calculate operational safe windows and target timelines.")

with st.form("milestone_inputs"):
    col1, col2 = st.columns(2)
    
    with col1:
        deal_name = st.text_input("Transaction Name / File Number", value="File #2026-884A (Commercial Plaza)")
        effective_date = st.date_input("Contract Effective Date", value=datetime.today().date())
        target_closing = st.date_input("Scheduled Closing Date")
        
    with col2:
        due_diligence_days = st.number_input("Due Diligence Window (Days)", min_value=1, max_value=180, value=30)
        financing_days = st.number_input("Financing Contingency Window (Days)", min_value=0, max_value=180, value=45)
        title_objection_days = st.number_input("Title Objection Review Window (Days)", min_value=1, max_value=30, value=10)

    submit_dates = st.form_submit_button("📅 Compute Timeline Map")

# 3. Operations Calculations Engine
# Project the exact calendar dates from the user parameters
due_diligence_deadline = effective_date + timedelta(days=due_diligence_days)
title_deadline = effective_date + timedelta(days=title_objection_days)
financing_deadline = effective_date + timedelta(days=financing_days)

# Calculate real-time day counts relative to today
days_until_dd = (due_diligence_deadline - now.date()).days
days_until_closing = (target_closing - now.date()).days

# 4. Interactive Timeline UI View
col_metrics1, col_metrics2 = st.columns(2)

with col_metrics1:
    st.markdown(f"### 📊 Project Timeline Status: **{deal_name}**")
    
    # Format layout for calculated deadlines
    st.info(f"📋 **Title Objection Deadline:** {title_deadline.strftime('%A, %b %d, %Y')}")
    st.info(f"💸 **Financing Contingency Expiration:** {financing_deadline.strftime('%A, %b %d, %Y')}")
    st.info(f"🤝 **Target Escrow Closing Date:** {target_closing.strftime('%A, %b %d, %Y')}")

with col_metrics2:
    st.markdown("### 🚦 Priority Action Metrics")
    
    # Calculate Due Diligence urgency metric
    if days_until_dd > 7:
        st.metric(label="Days to Earnest Money Hard Date", value=f"{days_until_dd} Days", delta="Safe Window")
    elif 0 <= days_until_dd <= 7:
        st.metric(label="Days to Earnest Money Hard Date", value=f"{days_until_dd} Days", delta="-URGENT ASSIST", delta_color="inverse")
    else:
        st.metric(label="Days to Earnest Money Hard Date", value="EXPIRED", delta="Funds Non-Refundable", delta_color="inverse")
        
    # Calculate Closing urgency metric
    if days_until_closing > 0:
        st.metric(label="Days Remaining Until Closing Day", value=f"{days_until_closing} Days")
    elif days_until_closing == 0:
        st.metric(label="🚀 CLOSING DAY TODAY", value="ACTIVE TARGET", delta="High Volume Workload")
    else:
        st.metric(label="Transaction Status", value="Closed/Past Target")

st.markdown("---")
st.subheader("💡 Automated Escrow Coordinator Insights")

# Output operational advisory flags
if days_until_closing == 14:
    st.warning("📣 **Escrow Task:** File is 14 days out from closing. Initiate pro-forma title insurance assembly and request final loan instructions from lender.")
elif 0 < days_until_closing <= 5:
    st.error("🚨 **Escrow Task:** Final crunch window. Request updated payoff letters, clear open schedule B title exceptions, and verify incoming buyer wire paths.")
else:
    st.success("Milestones mapped. Monitor the priority counters daily to avoid contract defaults.")
