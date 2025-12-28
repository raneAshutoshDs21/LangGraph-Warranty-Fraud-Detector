import streamlit as st
import pandas as pd
from main import process_claims

# =====================================================
# Page Config
# =====================================================
st.set_page_config(
    page_title="Azure OpenAI Warranty Fraud Detector",
    layout="wide"
)

# =====================================================
# Initialize state-safe variables (CRITICAL FIX)
# =====================================================
results_df = None
uploaded_df = None

if "results_df" in st.session_state:
    results_df = st.session_state["results_df"]

# =====================================================
# Global Styles
# =====================================================
st.markdown(
    """
    <style>
    .stApp { background-color: #f8fafc; color: #0f172a; font-family: "Segoe UI", sans-serif; }
    h1, h2, h3 { font-weight: 600; color: #020617; }

    .header {
        background: #ffffff;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 6px rgba(2,6,23,0.05);
        margin-bottom: 24px;
        text-align: center;
    }

    .card {
        background: #ffffff;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 6px rgba(2,6,23,0.04);
        margin-bottom: 16px;
    }

    .stButton > button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 10px 18px;
        font-weight: 600;
        border: none;
    }

    .kpi {
        background: #ffffff;
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        text-align: center;
    }

    .kpi-title { font-size: 13px; color: #64748b; }
    .kpi-value { font-size: 28px; font-weight: 700; margin-top: 6px; }

    .approve { color: #15803d; }
    .reject { color: #b91c1c; }
    .escalate { color: #b45309; }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# Header
# =====================================================
st.markdown(
    """
    <div class="header">
        <h1>Azure OpenAI Warranty Fraud Detector</h1>
        <div style="color:#475569;font-size:14px">
            Upload warranty claims, analyze fraud risk, review decisions
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# Upload & Actions
# =====================================================
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Upload Claims CSV")
    uploaded_file = st.file_uploader("Upload CSV", type=["csv"], label_visibility="collapsed")
    st.markdown("<small>One claim per row. Results include fraud score and agent decisions.</small>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Actions")
    generate_button = st.button("Run Fraud Detection", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# Processing
# =====================================================
if uploaded_file is not None:
    try:
        uploaded_df = pd.read_csv(uploaded_file)
        st.markdown("### Preview Uploaded Data")
        st.dataframe(uploaded_df.head(10), use_container_width=True)

        if generate_button:
            progress = st.progress(0)
            status = st.empty()

            def progress_cb(current, total):
                progress.progress(int((current / total) * 100))
                status.info(f"Processing {current}/{total}")

            with st.spinner("Analyzing claims..."):
                results_df = process_claims(uploaded_df, progress_callback=progress_cb)

            st.session_state["results_df"] = results_df
            status.success("Processing complete")

    except Exception as e:
        st.error(f"Failed to read CSV: {e}")
else:
    st.info("Please upload a CSV file to begin.")

# =====================================================
# Results
# =====================================================
if results_df is not None and not results_df.empty:

    st.markdown("## Results Summary")

    total = len(results_df)
    approves = (results_df["decision"] == "Approve claim").sum()
    rejects = (results_df["decision"] == "Reject claim").sum()
    escalates = (results_df["decision"] == "Escalate to HITL").sum()

    c1, c2, c3, c4 = st.columns(4)

    c1.markdown(f"<div class='kpi'><div class='kpi-title'>Total</div><div class='kpi-value'>{total}</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='kpi'><div class='kpi-title'>Approved</div><div class='kpi-value approve'>{approves}</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='kpi'><div class='kpi-title'>Rejected</div><div class='kpi-value reject'>{rejects}</div></div>", unsafe_allow_html=True)
    c4.markdown(f"<div class='kpi'><div class='kpi-title'>Escalated</div><div class='kpi-value escalate'>{escalates}</div></div>", unsafe_allow_html=True)

    st.markdown("## Detailed Results")
    st.dataframe(results_df, use_container_width=True)

    st.download_button(
        "Download Results CSV",
        results_df.to_csv(index=False).encode("utf-8"),
        "processed_claims.csv",
        "text/csv"
    )

    st.markdown("## Agent Conversation Trace")
    idx = st.selectbox("Select Claim", range(len(results_df)), format_func=lambda i: f"Claim {i+1}")

    trace = results_df.iloc[idx].get("agent_trace", [])
    if not trace:
        st.info("No agent trace available.")
    else:
        for step in trace:
            with st.expander(step.get("agent")):
                st.code(step.get("prompt", ""), language="")
                st.code(step.get("response", ""), language="")
