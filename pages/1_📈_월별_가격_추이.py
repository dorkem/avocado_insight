import streamlit as st
import plotly.express as px
from src.data_loader import load_avocado_data

df = load_avocado_data()
df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)

monthly_avg = (
    df.groupby(['YearMonth', 'type'])['AveragePrice']
    .mean()
    .reset_index()
)

fig = px.line(
    monthly_avg,
    x='YearMonth',
    y='AveragePrice',
    color='type',
    markers=True,
    title='월별 아보카도 평균 가격 (종류별)'
)

fig.update_layout(
    xaxis_title='월',
    yaxis_title='평균 가격 ($)',
    xaxis_tickangle=-45
)

st.plotly_chart(fig)
