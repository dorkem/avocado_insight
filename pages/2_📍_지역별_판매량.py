import pandas as pd
import plotly.express as px
import streamlit as st

from src.data_loader import load_avocado_data

st.title("🥑 지역별 아보카도 판매량 분석")

# 1. 데이터 로딩
df = load_avocado_data()

# 2. 지역별 총 판매량 계산 (TotalUS 제외)
region_volume = (
    df[df['region'] != 'TotalUS']
    .groupby('region')['Total Volume']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

top10 = region_volume.head(10)

# 3. Plotly로 시각화
fig = px.bar(
    top10,
    x='region',
    y='Total Volume',
    title='Top 10 지역별 아보카도 총 판매량',
    labels={'region': '지역', 'Total Volume': '총 판매량'},
    text_auto='.2s'  # 판매량 위에 라벨 추가 (예: 1.2M)
)

fig.update_layout(
    xaxis_tickangle=-45,
    yaxis_title='판매량',
    title_x=0.5  # 가운데 정렬
)

st.plotly_chart(fig)

# 4. 지역별 PLU별 판매량 비교
st.subheader("📊 지역별 PLU별 판매량 비교")

plu_df = df[['region', '4046', '4225', '4770']].copy()
for col in ['4046', '4225', '4770']:
    plu_df[col] = pd.to_numeric(plu_df[col], errors='coerce')

plu_by_region = plu_df.groupby('region')[['4046', '4225', '4770']].sum().reset_index()
plu_by_region['Top PLU'] = plu_by_region[['4046', '4225', '4770']].idxmax(axis=1)

st.dataframe(plu_by_region.sort_values(by='Top PLU', ascending=False).head(10))
