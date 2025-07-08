import pandas as pd
from pathlib import Path
import plotly.express as px
import streamlit as st

from src.data_loader import load_avocado_data

df = load_avocado_data()
df.head()

df['4046'] = pd.to_numeric(df['4046'], errors='coerce')
df['4225'] = pd.to_numeric(df['4225'], errors='coerce')
df['4770'] = pd.to_numeric(df['4770'], errors='coerce')
df['AveragePrice'] = pd.to_numeric(df['AveragePrice'], errors='coerce')

# 3개 PLU의 총합 계산
df['PLU_Total'] = df['4046'] + df['4225'] + df['4770']

# 각 PLU별 판매 비율
df['ratio_4046'] = df['4046'] / df['PLU_Total']
df['ratio_4225'] = df['4225'] / df['PLU_Total']
df['ratio_4770'] = df['4770'] / df['PLU_Total']

# PLU별 단가 근사치 계산
df['price_4046'] = df['AveragePrice'] * df['ratio_4046']
df['price_4225'] = df['AveragePrice'] * df['ratio_4225']
df['price_4770'] = df['AveragePrice'] * df['ratio_4770']

region_price_by_plu = df.groupby('region')[
    ['price_4046', 'price_4225', 'price_4770']
].mean().reset_index()

# 가장 저렴한 PLU 지역 찾기
cheap_4046 = region_price_by_plu.sort_values('price_4046').head(5)
cheap_4225 = region_price_by_plu.sort_values('price_4225').head(5)
cheap_4770 = region_price_by_plu.sort_values('price_4770').head(5)

heatmap_df = region_price_by_plu.melt(id_vars='region', 
                                       value_vars=['price_4046', 'price_4225', 'price_4770'],
                                       var_name='PLU_Code', 
                                       value_name='Avg_Price')

fig = px.density_heatmap(
    heatmap_df,
    x='PLU_Code',
    y='region',
    z='Avg_Price',
    color_continuous_scale='YlGnBu',
    text_auto='.2f',
    title='지역별 PLU 코드별 평균 단가 (근사값)'
)

fig.update_layout(
    xaxis_title="PLU 코드",
    yaxis_title="지역",
    height=900
)

st.plotly_chart(fig)
