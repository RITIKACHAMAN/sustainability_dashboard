import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO

def load_sample_data():
    rng = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
    units = ['Unit A', 'Unit B']
    departments = ['Spinning', 'Weaving', 'Dyeing']
    shifts = ['Morning', 'Evening', 'Night']
    rows = []
    np.random.seed(42)
    for d in rng:
        for u in units:
            for dept in departments:
                for shift in shifts:
                    rows.append({
                        'Date': d,
                        'Unit': u,
                        'Department': dept,
                        'Machine': f"M{np.random.randint(1,20)}",
                        'Shift': shift,
                        'Energy': int(np.random.normal(350, 60)),
                        'Water': int(np.random.normal(1800, 300)),
                        'Waste': int(np.random.normal(80, 20)),
                        'Emissions': int(np.random.normal(650, 100))
                    })
    df = pd.DataFrame(rows)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def get_kpis(df):
    return {
        'Energy': df['Energy'].sum(),
        'Water': df['Water'].sum(),
        'Waste': df['Waste'].sum(),
        'Emissions': df['Emissions'].sum()
    }

st.set_page_config(layout='wide', page_title='Sustainability Dashboard')
st.title('🌱 Sustainability Dashboard — Textile Company')

uploaded = st.sidebar.file_uploader('Upload CSV (optional)', type=['csv', 'xlsx'])
if uploaded is not None:
    try:
        df = pd.read_csv(uploaded, parse_dates=['Date'])
    except Exception:
        df = pd.read_excel(uploaded, parse_dates=['Date'])
else:
    df = load_sample_data()

if not np.issubdtype(df['Date'].dtype, np.datetime64):
    df['Date'] = pd.to_datetime(df['Date'])

st.sidebar.header('Filters')
min_date = df['Date'].min().date()
max_date = df['Date'].max().date()
date_range = st.sidebar.date_input('Date range', (min_date, max_date))
start_date, end_date = date_range

units = st.sidebar.multiselect('Unit', options=sorted(df['Unit'].unique()), default=list(df['Unit'].unique()))
depts = st.sidebar.multiselect('Department', options=sorted(df['Department'].unique()), default=list(df['Department'].unique()))
shifts = st.sidebar.multiselect('Shift', options=sorted(df['Shift'].unique()), default=list(df['Shift'].unique()))
machines = st.sidebar.multiselect('Machine', options=sorted(df['Machine'].unique()), default=list(df['Machine'].unique()))

mask = (
    (df['Date'].dt.date >= start_date) &
    (df['Date'].dt.date <= end_date) &
    (df['Unit'].isin(units)) &
    (df['Department'].isin(depts)) &
    (df['Shift'].isin(shifts)) &
    (df['Machine'].isin(machines))
)
filtered = df[mask].copy()

kpis = get_kpis(filtered)
col1, col2, col3, col4 = st.columns(4)
col1.metric('⚡ Energy (kWh)', f"{kpis['Energy']:,}")
col2.metric('💧 Water (L)', f"{kpis['Water']:,}")
col3.metric('🗑 Waste (kg)', f"{kpis['Waste']:,}")
col4.metric('🌫 Emissions (kg CO₂)', f"{kpis['Emissions']:,}")

st.subheader('Trend Over Time')
trend_df = filtered.groupby('Date').sum().reset_index()
if not trend_df.empty:
    trend_fig = px.line(trend_df, x='Date', y=['Energy','Water','Waste','Emissions'], markers=True)
    st.plotly_chart(trend_fig, use_container_width=True)
