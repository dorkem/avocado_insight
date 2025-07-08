# 🥑 Avocado Prices 데이터셋 설명

## 🔗 데이터셋 링크
https://www.kaggle.com/datasets/neuromusic/avocado-prices/data

## 📌 배경 (Context)

> 밀레니얼 세대는 아보카도 토스트를 너무 사랑해서 집을 못 산다  
> 그렇다면 아보카도가 저렴한 도시에서 산다면... 희망이 있을지도?

---

## 📥 데이터 출처
- **Hass Avocado Board**에서 제공한 2018년까지의 리테일 스캔 데이터
- 판매는 실제로 **소매점의 POS (판매시점정보)** 에서 수집됨
- 데이터는 여러 유통채널을 포함한 **다채널 리포트**:
  - 마트, 할인점, 클럽스토어, 약국, 1달러샵, 군 매장 등

---

## 📋 주요 컬럼 설명

| 컬럼명 | 의미 |
|--------|------|
| `Date` | 관측된 날짜 (주 단위) |
| `AveragePrice` | 아보카도 개당 평균 가격 |
| `type` | 아보카도 종류 (`conventional` or `organic`) |
| `year` | 연도 (예: 2015, 2016...) |
| `Region` | 판매가 발생한 도시 혹은 지역 (예: Albany, Los Angeles) |
| `Total Volume` | 해당 주간에 판매된 총 아보카도 수 |
| `4046`, `4225`, `4770` | 각각의 PLU 코드(제품 라벨 코드)를 가진 아보카도의 판매 수량 |
| `Total Bags` | 봉지 포장된 아보카도 총량 |
| `Small Bags`, `Large Bags`, `XLarge Bags` | 봉지 크기별 판매량 (소형/중형/대형) |

---

## 짤

<img width="480" height="699" alt="Image" src="https://github.com/user-attachments/assets/313a515b-b73c-4d7f-bcff-3227a096bfd2" />

---

## 📊 대시보드 미리보기

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/62e612f4-cdeb-4246-bafb-bebcfe648dd9" width="100%"/></td>
    <td><img src="https://github.com/user-attachments/assets/9203a7c2-74b6-4df2-87e8-8cbd2ef7dc18" width="100%"/></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/42a47c65-3811-4fe5-8b99-5e5ce0fa4591" width="100%"/></td>
    <td><img src="https://github.com/user-attachments/assets/896b38ca-a7d9-450e-8626-076eed8b57a0" width="100%"/></td>
  </tr>
</table>

---

## ⚙️ 사용 기술 스택

| 구분 | 내용 |
|------|------|
| 🐍 Python | 데이터 처리 및 로직 구현 |
| 📊 Pandas | 데이터프레임 처리, 그룹화, 전처리 등 |
| 📈 Plotly Express | 인터랙티브 시각화 (bar, line, heatmap 등) |
| 🌐 Streamlit | 웹 대시보드 UI 구성 |
| 📒 Jupyter Notebook | 분석 코드 작성 및 테스트 환경 |