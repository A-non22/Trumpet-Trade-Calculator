import streamlit as st

st.set_page_config(page_title="Trumpet Trade Calculator", layout="wide")

st.markdown(
    "<h1 style='text-align: center;'>Trumpet Trade Calculator</h1>",
    unsafe_allow_html=True
)

# Create two columns for the two calculators
col1, col2 = st.columns(2)

# ------------------- Updated Calculator 1: Trade Confidence -------------------
with col1:
    st.header("Trade Confidence")

    wdrr_seq = st.selectbox("WDRR Sequencing (Total credit -3)", options=[0, 1, 2, 3], key="wdrr_seq")
    ddr = st.selectbox("DDR (Total credit -2)", options=[0, 1, 2], key="ddr")
    m7box = st.selectbox("M7Box (Total credit -2)", options=[0, 1, 2], key="m7box")
    model = st.selectbox("Model (Total credit -2)", options=[0, 1, 2], key="model")
    bml = st.selectbox("BML (Total credit -1)", options=[0, 1], key="bml")
    wdrr_zero = st.selectbox("WDRR Zero Line (Total credit -1)", options=[0, 1], key="wdrr_zero")
    m7x_target = st.selectbox("M7X Target Hit (Total credit -1)", options=[0, 1], key="m7x_target")
    liquidity_swept = st.selectbox("Liquidity Swept (Total credit -1)", options=[0, 1], key="liquidity_swept")
    trumpet_symmetry = st.selectbox("Trumpet Trade - symmetry (Total credit -1)", options=[0, 1], key="trumpet_symmetry")

    obtained_credit_1 = (wdrr_seq + ddr + m7box + model +
                         bml + wdrr_zero + m7x_target + liquidity_swept + trumpet_symmetry)

    total_possible_credit_1 = 14  # Updated total with new input

    percentage_1 = (obtained_credit_1 / total_possible_credit_1) * 100 if total_possible_credit_1 > 0 else 0

    st.header("Results")
    st.markdown(
        f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit_1} / {total_possible_credit_1}</span></h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h3><b>Trade Confidence:</b> <span style='color:green;'>{percentage_1:.2f}%</span></h3>",
        unsafe_allow_html=True
    )

# ------------------- Updated Calculator 2: Entry Calculator -------------------
with col2:
    st.header("Entry Calculator")

    mdrc = st.selectbox("MDRC (Total credit -3)", options=[0, 1, 2, 3], key="mdrc")
    long_short = st.selectbox("Long/Short Structure (Total credit -2)", options=[0, 1, 2], key="long_short")
    svp_reject = st.selectbox("SVP Reject (Total credit -1)", options=[0, 1], key="svp_reject")
    bml_reject = st.selectbox("BML Reject (Total credit -1)", options=[0, 1], key="bml_reject")
    mb_reject = st.selectbox("MB Reject (Total credit -1)", options=[0, 1], key="mb_reject")
    db = st.selectbox("DB (Total credit -1)", options=[0, 1], key="db")
    wdrc_mid = st.selectbox("WDRC Mid (Total credit -1)", options=[0, 1], key="wdrc_mid")
    drc_reject = st.selectbox("DRC Reject (Total credit -1)", options=[0, 1], key="drc_reject")
    limiter_reject = st.selectbox("Limiter Reject (Total credit -1)", options=[0, 1], key="limiter_reject")
    drib_reject = st.selectbox("Drib Reject (Total credit -1)", options=[0, 1], key="drib_reject")
    m7box_reject = st.selectbox("M7Box Reject (Total credit -1)", options=[0, 1], key="m7box_reject")
    ddr_line_reject = st.selectbox("DDR Line Rejection (Total credit -1)", options=[0, 1], key="ddr_line_reject")
    wdrr_line_reject = st.selectbox("WDRR Line Rejection (Total credit -1)", options=[0, 1], key="wdrr_line_reject")
    half_reject = st.selectbox("0.5 Reject (Total credit -1)", options=[0, 1], key="half_reject")
    wdr_reject = st.selectbox("WDR reject (Total credit -1)", options=[0, 1], key="wdr_reject")  # NEW INPUT

    obtained_credit_2 = (
        mdrc + long_short + svp_reject + bml_reject + mb_reject +
        db + wdrc_mid + drc_reject + limiter_reject + drib_reject +
        m7box_reject + ddr_line_reject + wdrr_line_reject + half_reject + wdr_reject
    )

    total_possible_credit_2 = 18  # Updated for new input

    percentage_2 = (obtained_credit_2 / total_possible_credit_2) * 100 if total_possible_credit_2 > 0 else 0

    st.header("Results")
    st.markdown(
        f"<h3><b>Obtained Credit:</b> <span style='color:green;'>{obtained_credit_2} / {total_possible_credit_2}</span></h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<h3><b>Entry Quality:</b> <span style='color:green;'>{percentage_2:.2f}%</span></h3>",
        unsafe_allow_html=True
    )
