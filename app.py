import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Solar & Weather Data Dashboard")

# Select Country
country = st.selectbox("Select a Country", ["nigeria", "ethiopia", "kenya", "sudan", "tanzania"])

# Load Data
df = pd.read_csv(f'data/{country}.csv').replace(-999, pd.NA)

# Show Stats
st.subheader(f"Summary Statistics for {country.title()}")
st.write(df[['T2M', 'PRECTOTCORR', 'RH2M', 'WS2M']].describe())

# Visual: Heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df[['T2M', 'PRECTOTCORR', 'RH2M', 'WS2M']].corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)