import pandas as pd
import numpy as np
import os
import streamlit as st
from datetime import date
from plotly import graph_objs as go
import seaborn as sns

@st.cache
def get_data():
    return pd.read_csv(r"/Users/Marco/Documents/web_report_test/test_report.csv")
df = get_data()

st.title('Test Report')
selected_country = st.selectbox('Select Country for prediction', df["Country"].unique())
selected_sector = st.selectbox('Select Sector for prediction', df["Sector"].unique())
n_years = st.slider('Years of prediction:', 2020, 2021)
n_months = st.slider('Months of prediction:', df.Month.min(), df.Month.max())
pivot = df.groupby(['Country','Sector','Year','Month']).agg(Sum=('Value', 'sum')).reset_index()

report = pivot[(pivot.Country == selected_country) & (pivot.Sector== selected_sector)]

st.subheader("Report per country/sector")
st.write(report)

def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=report['Month'], y=report['Sum'], mode='lines',  name="stock_open"))
	fig.layout.update(title_text='Time Series',)
	st.plotly_chart(fig)
	
plot_raw_data()


