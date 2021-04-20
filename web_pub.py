import pandas as pd
import numpy as np
import base64
import os
import streamlit as st
from datetime import date
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
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

csv = report.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;file_name&gt;.csv)'
st.markdown(href, unsafe_allow_html=True)

def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=report['Month'], y=report['Sum'], mode='lines',  name="stock_open"))
	fig.layout.update(title_text='Time Series',)
	st.plotly_chart(fig)
	
plot_raw_data()


