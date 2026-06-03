import streamlit as st
from datetime import datetime, timedelta, time
import pytz

st.title("⏰ Critical Date & Wire Deadline Alerts")

# 1. Timezone & Bank Cutoff Controls
st.sidebar.header("⚙️ Wire Deadline Settings")

tz_options = {
    "Eastern Time (NY Corp HQ)": "US/Eastern",
    "Central Time (Texas/Midwest)": "US/Central",
    "Mountain Time": "US/Mountain",
    "Pacific Time (West Coast)": "US/Pacific"
}
selected_tz_label = st.sidebar.selectbox("Your Operating Timezone", list(tz_options.keys()))
local_tz = pytz.timezone(tz_options[selected_tz_label])

bank_cutoffs = {
    "Standard Fedwire (Absolute Limit)": "18:00",
    "Commercial Settlement Bank (Typical)": "16:30",
    "Priority Closing Cutoff (Fast-Track)": "15:30",
    "Custom Cutoff Time": "Custom"
}
selected_bank_cutoff = st.sidebar.selectbox("Bank Processing Cutoff", list(bank_cutoffs.keys()), index=1)

if selected_bank_cutoff == "Custom":
    custom_time = st.sidebar.time_input("Set Custom Wire Deadline", value=datetime.strptime("16:30", "%H:%M").time())
    cutoff_hour, cutoff_min = custom_time.hour, custom_time.minute
else:
    time_str = bank_cutoffs[selected_bank_cutoff]
    cutoff_hour, cutoff_min = map(int, time_str.split(":"))

# 2. Wire Cutoff Priority Dashboard
st.subheader("🚨 Real-Time Wire Deadline Tracking")

now_utc = datetime.now(pytz.utc)
now_local = now_utc.astimezone(local_tz)
cutoff_time_local = now_local.replace(hour=cutoff_hour, minute=cutoff_min, second=0, microsecond=0)

col_clock1, col_clock2 = st.columns(2)
with col_clock1:
    st.metric("🕰️ Your Local Desk Time", now_local.strftime("%I:%M %p (%Z)"))
with col_clock2:
    st.metric("🎯 Selected Target Deadline", cutoff_time_local.strftime("%I:%M %p (%Z)"))

if now_local < cutoff_time_local:
    time_remaining = cutoff_time_local - now_local
    hours, remainder = divmod(time_remaining.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    
    if hours < 1:
        st.error(f"🔴 **CRITICAL WIRE CRUNCH:** Only **{minutes} minutes** remaining before the {selected_bank_cutoff} ({cutoff_time_local.strftime('%I:%M %p')})! Route final funding packets immediately.")
    elif hours < 2:
        st.warning(f"🟡 **Approaching Cutoff:** **{hours} hour and {minutes} minutes** left to approve outbound disbursements for same-day settlement.")
    else:
        st.success(f"🟢 **Wire Window Stable:** **{hours} hours and {minutes} minutes** remaining until the scheduled bank cutoff.")
else:
    st.error(f"🛑 **Same-Day Processing Closed:** The {cutoff_time_local.strftime('%I:%M %p')} deadline has passed. Wires moved now will default to next business day credit.")

st.markdown("---")

# 3. Pipeline Milestone Tracking Matrix
st.subheader("📂 Active Transaction Milestone Audit")
st.write("Input deal milestones to instantly calculate operational safe windows and target timelines.")

with st.form("milestone_inputs"):
    col1, col2 = st.columns(2)
    
    with col1:
        deal_name = st.text_input("Transaction Name / File Number", value="File #2026-884A (Commercial Plaza)")
        effective_date = st.date_input("Contract Effective Date", value=now_local.date())
        target_closing = st.date_input("Scheduled Closing Date", value=now_local.date() + timedelta(days=45))
        
    with col2:
        due_diligence_days = st.number_input("Due Diligence Window (Days)", min_value=1, max_value=180, value=30)
        financing_days = st.number_input("Financing Contingency Window (Days)", min_value=0, max_value=180, value=45)
        title_objection_days = st.number_input("Title Objection Review Window (Days)", min_value=1, max_value=30, value=10)

    submit_dates = st.form_submit_button("📅 Compute Timeline Map")

# 4. Operations Calculations Engine
due_diligence_deadline = effective_date + timedelta(days=due_diligence_days)
title_deadline = effective_date + timedelta(days=title_objection_days)
financing_deadline = effective_date + timedelta(days=financing_days)

days_until_dd = (due_diligence_deadline - now_local.date()).days
days_until_closing = (target_closing - now_local.date()).days

# 5. Interactive Timeline UI View
col_metrics1, col_metrics2 = st.columns(2)

with col_metrics1:
    st.markdown(f"### 📊 Project Timeline Status: **{deal_name}**")
    st.info(f"📋 **Title Objection Deadline:** {title_deadline.strftime('%A, %b %d, %Y')}")
    st.info(f"💸 **Financing Contingency Expiration:** {financing_deadline.strftime('%A, %b %d, %Y')}")
    st.info(f"🤝 **Target Escrow Closing Date:** {target_closing.strftime('%A, %b %d, %Y')}")

with col_metrics2:
    st.markdown("### 🚦 Priority Action Metrics")
    
    if days_until_dd > 7:
        st.metric(label="Days to Earnest Money Hard Date", value=f"{days_until_dd} Days", delta="Safe Window")
    elif 0 <= days_until_dd <= 7:
        st.metric(label="Days to Earnest Money Hard Date", value=f"{days_until_dd} Days", delta="-URGENT ASSIST", delta_color="inverse")
    else:
        st.metric(label="Days to Earnest Money Hard Date", value="EXPIRED", delta="Funds Non-Refundable", delta_color="inverse")
        
    if days_until_closing > 0:
        st.metric(label="Days Remaining Until Closing Day", value=f"{days_until_closing} Days")
    elif days_until_closing == 0:
        st.metric(label="🚀 CLOSING DAY TODAY", value="ACTIVE TARGET", delta="High Volume Workload")
    else:
        st.metric(label="Transaction Status", value="Closed/Past Target")

st.markdown("---")
st.subheader("💡 Automated Escrow Coordinator Insights")

if days_until_closing == 14:
    st.warning("📣 **Escrow Task:** File is exactly 14 days out from closing. Initiate pro-forma title insurance assembly and request loan instructions.")
elif 0 < days_until_closing <= 5:
    st.error("🚨 **Escrow Task:** Final crunch window. Request updated payoff letters, clear open schedule B title exceptions, and verify incoming wire paths.")
else:
    st.success("Milestones mapped. Monitor the priority counters daily to keep transaction tracks clear of defaults.")
