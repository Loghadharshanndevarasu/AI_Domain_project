"""IT Services Cloud Migration & Intelligent Automation Management Portal."""

from datetime import datetime

import pandas as pd
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(
	page_title="CloudOps Command Center",
	page_icon="C",
	layout="wide",
	initial_sidebar_state="expanded",
)


# Keep the visual language compact and operational, with a single accent color.
st.markdown(
	"""
	<style>
	@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Space+Grotesk:wght@400;500;600;700&display=swap');

	:root {
		--ink: #17232e;
		--muted: #667682;
		--line: #dce5e8;
		--paper: #f5f8f7;
		--panel: #ffffff;
		--teal: #087f78;
		--teal-soft: #e5f3f0;
		--amber: #b36b00;
		--red: #bf3b3b;
	}
	html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; color: var(--ink); }
	.stApp { background: var(--paper); }
	[data-testid="stSidebar"] { background: #eaf1ef; border-right: 1px solid var(--line); }
	[data-testid="stSidebar"] .block-container { padding-top: 2.3rem; }
	h1, h2, h3 { letter-spacing: 0; color: var(--ink); }
	h1 { font-size: 2.1rem !important; font-weight: 700 !important; }
	h2 { font-size: 1.3rem !important; }
	h3 { font-size: 1rem !important; }
	.eyebrow { color: var(--teal); font-family: 'DM Mono', monospace; font-size: .72rem; letter-spacing: .08em; text-transform: uppercase; }
	.subtle { color: var(--muted); font-size: .92rem; }
	.status-pill { display: inline-block; padding: .35rem .6rem; border-radius: 3px; background: var(--teal-soft); color: var(--teal); font-family: 'DM Mono', monospace; font-size: .72rem; }
	.section-rule { border-top: 1px solid var(--line); margin: 1.4rem 0; }
	[data-testid="stMetric"] { background: var(--panel); border: 1px solid var(--line); border-radius: 4px; padding: 1rem 1.1rem; }
	[data-testid="stMetricLabel"] { color: var(--muted); }
	[data-testid="stMetricValue"] { color: var(--ink); font-family: 'DM Mono', monospace; }
	.alert-row { border-left: 4px solid var(--teal); background: var(--panel); border-top: 1px solid var(--line); border-right: 1px solid var(--line); border-bottom: 1px solid var(--line); border-radius: 3px; padding: .75rem 1rem; margin: .5rem 0; }
	.alert-row.critical { border-left-color: var(--red); }
	.alert-row.warning { border-left-color: var(--amber); }
	.alert-meta { color: var(--muted); font-family: 'DM Mono', monospace; font-size: .72rem; }
	.result-box { background: var(--teal-soft); border: 1px solid #b8ded7; border-radius: 4px; padding: 1rem 1.2rem; }
	.result-box strong { color: var(--teal); }
	div.stButton > button { border-radius: 3px; border: 1px solid var(--teal); color: var(--teal); font-weight: 600; }
	div.stButton > button[kind="primary"] { background: var(--teal); color: white; }
	</style>
	""",
	unsafe_allow_html=True,
)


def cost_figure() -> go.Figure:
	"""Build the twelve-month cost comparison used by the executive view."""
	months = ["Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"]
	legacy = [182, 185, 188, 190, 194, 197, 201, 202, 204, 207, 209, 212]
	cloud = [176, 174, 169, 164, 158, 151, 147, 142, 136, 131, 126, 120]
	figure = go.Figure()
	figure.add_trace(go.Scatter(x=months, y=legacy, mode="lines+markers", name="Legacy estate", line=dict(color="#9aa9ad", width=2)))
	figure.add_trace(go.Scatter(x=months, y=cloud, mode="lines+markers", name="Cloud estate", line=dict(color="#087f78", width=3)))
	figure.update_layout(
		height=350,
		margin=dict(l=8, r=12, t=18, b=8),
		paper_bgcolor="rgba(0,0,0,0)",
		plot_bgcolor="rgba(0,0,0,0)",
		hovermode="x unified",
		yaxis=dict(title="Monthly cost ($k)", gridcolor="#e5ecec", zeroline=False),
		xaxis=dict(showgrid=False),
		legend=dict(orientation="h", y=1.12, x=0),
		font=dict(family="Space Grotesk, sans-serif", color="#17232e"),
	)
	return figure


def analyze_ticket(ticket: str) -> tuple[str, str, float, str]:
	"""Classify common operational signals without requiring an external AI key."""
	normalized = ticket.lower()
	critical_terms = ("outage", "down", "ransomware", "breach", "data loss", "production")
	warning_terms = ("slow", "latency", "timeout", "error", "failed", "unavailable")
	if any(term in normalized for term in critical_terms):
		severity = "SEV-1 / Critical"
		fix = "Route to the incident bridge, fail over the affected workload, and enable an automated rollback runbook."
		hours = 4.5
		tone = "critical"
	elif any(term in normalized for term in warning_terms):
		severity = "SEV-2 / High"
		fix = "Create a monitored remediation workflow that scales the service, clears the queue, and opens a tracked change."
		hours = 2.5
		tone = "warning"
	else:
		severity = "SEV-3 / Standard"
		fix = "Add a self-service knowledge response and an event-triggered ticket enrichment workflow."
		hours = 1.0
		tone = "standard"
	return severity, fix, hours, tone


def render_header() -> None:
	st.markdown('<div class="eyebrow">NORTHSTAR / CLOUD OPERATIONS</div>', unsafe_allow_html=True)
	st.title("Migration & Intelligent Automation")
	st.markdown('<span class="status-pill">SYSTEMS NOMINAL</span> &nbsp; <span class="subtle">Operations portfolio · August 2026</span>', unsafe_allow_html=True)


def render_dashboard() -> None:
	st.markdown("### Executive Dashboard")
	st.markdown('<p class="subtle">A live view of the migration program and automation return.</p>', unsafe_allow_html=True)
	metrics = st.columns(4)
	metrics[0].metric("Cost saved", "$742k", "+18.4%")
	metrics[1].metric("Cloud availability", "99.97%", "+0.08%")
	metrics[2].metric("Tickets automated", "12,480", "+31.2%")
	metrics[3].metric("Apps migrated", "68 / 94", "72.3%")
	st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)
	chart_col, notes_col = st.columns([2.2, 1])
	with chart_col:
		st.markdown("### Run-rate cost trajectory")
		st.plotly_chart(cost_figure(), use_container_width=True, config={"displayModeBar": False})
	with notes_col:
		st.markdown("### Program signals")
		st.info("Cloud run-rate is 43% below the projected legacy estate this month.")
		st.success("Three migration waves completed this quarter.")
		st.warning("Database modernization is the current schedule constraint.")


def render_analyzer() -> None:
	st.markdown("### GenAI Incident Analyzer")
	st.markdown('<p class="subtle">Turn an incoming support ticket into a first-response action plan.</p>', unsafe_allow_html=True)
	ticket = st.text_area(
		"Paste an IT support ticket",
		placeholder="Example: Production checkout API is timing out for customers in us-east-1...",
		height=170,
	)
	if st.button("Analyze incident", type="primary", use_container_width=False):
		if not ticket.strip():
			st.warning("Add a ticket description before analyzing.")
		else:
			severity, fix, hours, tone = analyze_ticket(ticket)
			st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)
			result_cols = st.columns([1, 1, 1])
			result_cols[0].metric("Predicted severity", severity)
			result_cols[1].metric("Estimated hours saved", f"{hours:.1f} hrs")
			result_cols[2].metric("Automation confidence", "92%")
			st.markdown(f'<div class="result-box"><strong>Recommended cloud automation</strong><br>{fix}</div>', unsafe_allow_html=True)
			st.caption(f"Analysis mode: deterministic triage rules · signal class: {tone}")


def render_readiness() -> None:
	st.markdown("### Cloud Readiness Matrix")
	st.markdown('<p class="subtle">Migration strategy, readiness score, and next action across the application estate.</p>', unsafe_allow_html=True)
	readiness = pd.DataFrame(
		[
			["Customer Portal", "Rehost", 92, "Wave 1", "Ready"],
			["Order Processing", "Refactor", 76, "Wave 2", "In assessment"],
			["Finance Ledger", "Replace", 61, "Wave 3", "Vendor shortlist"],
			["Identity Service", "Refactor", 88, "Wave 1", "Ready"],
			["Reporting Hub", "Replace", 54, "Wave 4", "Discovery"],
			["Support Console", "Rehost", 97, "Wave 1", "Ready"],
			["Inventory API", "Refactor", 81, "Wave 2", "In assessment"],
		],
		columns=["Application", "Strategy", "Readiness %", "Migration wave", "Status"],
	)
	strategy = st.multiselect("Filter strategy", ["Rehost", "Refactor", "Replace"], default=["Rehost", "Refactor", "Replace"])
	st.dataframe(readiness[readiness["Strategy"].isin(strategy)], use_container_width=True, hide_index=True)


def render_security() -> None:
	st.markdown("### Security & DevOps")
	st.markdown('<p class="subtle">Live operational signals and compliance posture across the delivery platform.</p>', unsafe_allow_html=True)
	status_col, compliance_col = st.columns([1.1, 1.9])
	with status_col:
		st.markdown("### Compliance posture")
		st.metric("Controls passing", "46 / 48", "95.8%")
		st.progress(0.958)
		st.success("SOC 2 evidence collection on track")
		st.warning("2 medium findings due in 12 days")
	with compliance_col:
		st.markdown("### Control indicators")
		controls = pd.DataFrame({"Control": ["IAM least privilege", "Encryption at rest", "Backup recovery", "Vulnerability SLA"], "Status": ["PASS", "PASS", "PASS", "REVIEW"], "Owner": ["Platform", "Security", "SRE", "AppSec"]})
		st.dataframe(controls, use_container_width=True, hide_index=True)
	st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)
	st.markdown("### Real-time system log alerts")
	if st.button("Refresh alerts"):
		st.rerun()
	current_time = datetime.now().strftime("%H:%M:%S")
	alerts = [("CRITICAL", "payments-api", "Elevated 5xx rate detected; failover workflow armed.", "critical", "2 min ago"), ("WARNING", "identity-service", "Token refresh latency above 400 ms threshold.", "warning", "8 min ago"), ("INFO", "migration-runner", "Wave 18 validation completed successfully.", "standard", "14 min ago")]
	for level, service, message, tone, age in alerts:
		st.markdown(f'<div class="alert-row {tone}"><strong>{level}</strong> &nbsp; {message}<br><span class="alert-meta">{service} · {age} · polled {current_time}</span></div>', unsafe_allow_html=True)


render_header()
with st.sidebar:
	st.markdown('<div class="eyebrow">PORTFOLIO CONTROL</div>', unsafe_allow_html=True)
	st.markdown("### CloudOps / 26.08")
	st.markdown('<p class="subtle">Owner: Enterprise Technology<br>Region: Global production</p>', unsafe_allow_html=True)
	st.markdown('<div class="section-rule"></div>', unsafe_allow_html=True)
	st.caption("Last data sync")
	st.markdown("**08:42 UTC**")
	st.caption("Environment")
	st.markdown("**Production · 12 regions**")

dashboard_tab, analyzer_tab, readiness_tab, security_tab = st.tabs([
	"Executive Dashboard",
	"GenAI Incident Analyzer",
	"Cloud Readiness Matrix",
	"Security & DevOps",
])

with dashboard_tab:
	render_dashboard()
with analyzer_tab:
	render_analyzer()
with readiness_tab:
	render_readiness()
with security_tab:
	render_security()
