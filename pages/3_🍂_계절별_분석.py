# pages/seasonal_analysis.py

import pandas as pd
import plotly.express as px
import streamlit as st

from src.data_loader import load_avocado_data

st.title("🍂 계절별 아보카도 분석")
st.caption("유기농 vs 일반 아보카도의 계절별 평균 가격 및 판매량 비교")

# 1. 데이터 로딩
df = load_avocado_data()

# 2. 계절 컬럼 생성
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

df['season'] = df['Date'].dt.month.apply(get_season)

# 3. 계절별 평균 가격 계산
seasonal_price = df.groupby(['season', 'type'])['AveragePrice'].mean().reset_index()
fig_price = px.bar(
    seasonal_price,
    x='season',
    y='AveragePrice',
    color='type',
    barmode='group',
    title='계절별 평균 아보카도 가격 (유기농 vs 일반)',
    labels={'season': '계절', 'AveragePrice': '평균 가격 ($)'}
)
st.plotly_chart(fig_price)

# 4. 계절별 총 판매량 계산
seasonal_volume = df.groupby(['season', 'type'])['Total Volume'].sum().reset_index()
fig_volume = px.bar(
    seasonal_volume,
    x='season',
    y='Total Volume',
    color='type',
    barmode='group',
    title='계절별 총 판매량 (유기농 vs 일반)',
    labels={'season': '계절', 'Total Volume': '총 판매량'}
)
st.plotly_chart(fig_volume)

# 구분선
st.markdown("---")

# 5. 전체 판매량 비교 (유기농 vs 일반)
st.subheader("🟢 유기농 vs 일반 전체 판매량 비교")

total_volume_by_type = df.groupby('type')['Total Volume'].sum().reset_index()

fig_total = px.bar(
    total_volume_by_type,
    x='type',
    y='Total Volume',
    title='유기농 vs 일반 아보카도 전체 판매량 비교',
    labels={'type': '아보카도 종류', 'Total Volume': '총 판매량'},
    text='Total Volume',
    color='type',
    color_discrete_map={
        'organic': 'red',
        'conventional': '#636EFA'
    }
)

fig_total.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig_total.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

st.plotly_chart(fig_total)
