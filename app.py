import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="PM2.5 Dashboard", layout="wide")

st.title("🌫️ Bangkok Air Quality Dashboard")

st.markdown("""
This dashboard visualizes **PM2.5 trends, forecasts, and anomalies**
to support environmental awareness in Bangkok.
""")

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("final_dataset.csv", parse_dates=["date"])
    return df

df = load_data()

# =========================
# SIDEBAR
# =========================
st.sidebar.header("Filter")

start_date = st.sidebar.date_input("Start Date", df["date"].min())
end_date = st.sidebar.date_input("End Date", df["date"].max())

df = df[(df["date"] >= pd.to_datetime(start_date)) &
        (df["date"] <= pd.to_datetime(end_date))]

# =========================
# KPIs
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("Avg PM2.5", f"{df['pm2_5'].mean():.2f}")
col2.metric("Max PM2.5", f"{df['pm2_5'].max():.2f}")
col3.metric("Anomaly Days", int(df["anomaly"].sum()))

# =========================
# TABS
# =========================
tab1, tab2, tab3 = st.tabs(["📈 Trends", "🔮 Prediction", "⚠️ Anomalies"])

# =========================
# 📈 TRENDS
# =========================
with tab1:
    st.subheader("PM2.5 Trend Over Time")

    fig = px.line(df, x="date", y="pm2_5")

    st.plotly_chart(fig, use_container_width=True)

    st.info("This chart shows historical PM2.5 levels and seasonal patterns.")

# =========================
# 🔮 PREDICTION
# =========================
with tab2:
    st.subheader("Prediction vs Actual")

    if "prediction" in df.columns:
        fig2 = px.line(df, x="date", y=["pm2_5", "prediction"])

        st.plotly_chart(fig2, use_container_width=True)

        latest_pred = df["prediction"].iloc[-1]

        st.metric("Next Day Prediction", f"{latest_pred:.2f}")

    else:
        st.warning("Prediction data not available")

# =========================
# ⚠️ ANOMALIES
# =========================
# =========================
# ⚠️ ANOMALIES
# =========================
with tab3:
    st.subheader("Detected Anomalies")

    if "anomaly" in df.columns:
        # IMPORTANT: create a copy to avoid warning
        df_plot = df.copy()

        # Convert to label (THIS IS THE FIX)
        df_plot["anomaly_label"] = df_plot["anomaly"].map({
            0: "Normal",
            1: "Anomaly"
        })

        fig3 = px.scatter(
            df_plot,
            x="date",
            y="pm2_5",
            color="anomaly_label",
            category_orders={"anomaly_label": ["Normal", "Anomaly"]},
            color_discrete_map={
                "Normal": "blue",
                "Anomaly": "red"
            },
        )

        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("🔴 Red = Anomaly | 🔵 Blue = Normal")

    else:
        st.warning("Anomaly data not available")

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("Built with Streamlit • Data Science Project")