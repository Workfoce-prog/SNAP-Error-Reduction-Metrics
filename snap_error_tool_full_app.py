
import streamlit as st
import pandas as pd

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("SNAP_Error_Reduction_Full_Metrics.csv")

df = load_data()

st.title("📉 SNAP Error Reduction Risk Review Tool – Full Metrics")

# Sidebar filters
st.sidebar.header("Filter Households")
aef_only = st.sidebar.checkbox("Only show AEF flagged", value=False)
high_spers = st.sidebar.slider("Minimum SPERS Score", 0, 100, 0)

# Apply filters
filtered_df = df.copy()
if aef_only:
    filtered_df = filtered_df[filtered_df["AEF_Flag"] == True]
filtered_df = filtered_df[filtered_df["SPERS_Score"] >= high_spers]

# Show filtered table
st.subheader("Filtered Household Risk View")
st.dataframe(filtered_df)

# Individual household viewer
st.subheader("Household Detail View")
selected_id = st.selectbox("Select Household ID", df["Household_ID"])
selected = df[df["Household_ID"] == selected_id].iloc[0]

st.markdown(f"""
**SPERS Score:** {selected.SPERS_Score}  
**AEF Flag:** {'✅ Yes' if selected.AEF_Flag else '❌ No'}  
**Case Complexity (CCI):** {selected.CCI_Score}  
**Worker Error Count:** {selected.WAF_Error_Count}  
**Documentation Score:** {selected.DCS_Percent}%  
**Recertification Delay:** {selected.TRM_Days_Late} days  
**AI Validator Level:** {selected.Validator_Risk_Level}  

**ID Verification Risk Score:** {selected.ID_VERIFICATION_RISK_SCORE}  
**Income Volatility Index:** {selected.INCOME_VOLATILITY_INDEX}  
**Multi-Program Conflict Score:** {selected.MULTI_PROGRAM_CONFLICT_SCORE}  
**High-Balance Retention Score:** {selected.HIGH_BALANCE_RETENTION_SCORE}  
**ML Cluster ID:** {selected.ML_CLUSTER_ID}
""")
